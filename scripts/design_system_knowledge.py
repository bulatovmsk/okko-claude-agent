#!/usr/bin/env python3
"""Validate the Okko design-system knowledge contracts and build agent context."""

from __future__ import annotations

import argparse
import json
import re
import sys
import tempfile
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Sequence, Tuple


ROOT = Path(__file__).resolve().parents[1]
DS = Path("design-system")
PATHS = {
    "lifecycle": DS / "registry/lifecycle.json",
    "libraries": DS / "registry/libraries.json",
    "components": DS / "components/figma-sources.json",
    "mappings": DS / "mappings/platform-mappings.json",
    "cases": DS / "knowledge/cases.json",
    "gaps": DS / "knowledge/gaps.json",
    "index": DS / "generated/agent-index.json",
    "context": DS / "generated/agent-context.md",
}
PLATFORM_ALIASES = {
    "android": "android",
    "ios": "ios",
    "tv": "tv",
    "web": "web",
}
ID_PATTERN = re.compile(r"^[a-z0-9-]+$")
QUARTER_PATTERN = re.compile(r"^20\d{2}-Q[1-4]$")


class KnowledgeError(RuntimeError):
    pass


def load_json(path: Path) -> Dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as error:
        raise KnowledgeError(f"Не найден файл: {path}") from error
    except json.JSONDecodeError as error:
        raise KnowledgeError(f"Некорректный JSON {path}: {error}") from error
    if not isinstance(value, dict):
        raise KnowledgeError(f"Корень {path} должен быть JSON-объектом")
    return value


def require(condition: bool, message: str) -> None:
    if not condition:
        raise KnowledgeError(message)


def require_fields(record: Dict[str, Any], fields: Iterable[str], label: str) -> None:
    missing = sorted(set(fields) - set(record))
    require(not missing, f"{label}: отсутствуют поля {missing}")


def unique_records(records: Sequence[Dict[str, Any]], key: str, label: str) -> Dict[str, Dict[str, Any]]:
    result: Dict[str, Dict[str, Any]] = {}
    for record in records:
        value = record.get(key)
        require(isinstance(value, str) and bool(value), f"{label}: пустое поле {key}")
        require(value not in result, f"{label}: дублируется {key} `{value}`")
        result[value] = record
    return result


def normalize_platform(value: Any) -> str:
    normalized = str(value or "").strip().lower()
    require(normalized in PLATFORM_ALIASES, f"Неизвестная платформа: {value!r}")
    return PLATFORM_ALIASES[normalized]


def validate_lifecycle(data: Dict[str, Any]) -> Dict[str, Dict[str, Any]]:
    require(data.get("schemaVersion") == 1, "lifecycle: нужна schemaVersion 1")
    require(data.get("defaultStatus") == "ready", "lifecycle: defaultStatus должен быть ready")
    statuses = data.get("statuses")
    require(isinstance(statuses, list), "lifecycle: statuses должен быть массивом")
    by_id = unique_records(statuses, "id", "lifecycle")
    expected = {"planned", "work-in-progress", "design-only", "ready", "deprecated"}
    require(set(by_id) == expected, f"lifecycle: ожидаются статусы {sorted(expected)}")
    markers = [record.get("marker") for record in statuses]
    require(all(isinstance(marker, str) and marker for marker in markers), "lifecycle: у статуса нет marker")
    require(len(set(markers)) == len(markers), "lifecycle: markers должны быть уникальными")
    require(by_id["ready"].get("automaticUse") is True, "lifecycle: только ready должен разрешать automaticUse")
    for status, record in by_id.items():
        if status != "ready":
            require(record.get("automaticUse") is False, f"lifecycle: {status} не может использоваться автоматически")
    return by_id


def validate_libraries(data: Dict[str, Any]) -> Dict[str, Dict[str, Any]]:
    require(data.get("schemaVersion") == 1, "libraries: нужна schemaVersion 1")
    records = data.get("libraries")
    require(isinstance(records, list), "libraries: libraries должен быть массивом")
    by_id = unique_records(records, "id", "libraries")
    required_ids = {
        "lib-android", "lib-ios", "lib-tv", "lib-web",
        "okko-head", "tokens-mobile-web", "tokens-tv",
    }
    require(set(by_id) == required_ids, f"libraries: ожидаются записи {sorted(required_ids)}")
    for library_id, record in by_id.items():
        require(ID_PATTERN.fullmatch(library_id) is not None, f"libraries: некорректный id {library_id}")
        require_fields(
            record,
            {"name", "kind", "status", "platforms", "deviceClasses", "source", "dependencies"},
            f"library {library_id}",
        )
        require(record["kind"] in {"assets", "components", "tokens"}, f"library {library_id}: неизвестный kind")
        require(record["status"] in {"active", "pending-source"}, f"library {library_id}: неизвестный status")
        platforms = [normalize_platform(item) for item in record["platforms"]]
        require(len(platforms) == len(set(platforms)), f"library {library_id}: платформы дублируются")
        source = record["source"]
        if record["status"] == "active":
            require(isinstance(source, dict), f"library {library_id}: active-библиотеке нужен source")
            require_fields(source, {"fileKey", "url"}, f"library {library_id} source")
        else:
            require(source is None, f"library {library_id}: pending-source должен иметь source=null")
        for dependency in record["dependencies"]:
            require(dependency in by_id, f"library {library_id}: неизвестная зависимость {dependency}")
            require(dependency != library_id, f"library {library_id}: циклическая ссылка на себя")
    return by_id


def component_status(record: Dict[str, Any]) -> str:
    status = str((record.get("snapshot") or {}).get("status") or "")
    if record.get("kind") == "collection" and status == "collection":
        return "ready"
    if status:
        return status
    name = str(record.get("name") or "")
    lowered = name.lower()
    if name.startswith("🔴") or "[deprecated]" in lowered:
        return "deprecated"
    if name.startswith("⚪") or "[planned]" in lowered:
        return "planned"
    if "🟡" in name or "[нет в проде]" in lowered:
        return "work-in-progress"
    if name.startswith("🔵") or "[design-only]" in lowered or "[design only]" in lowered:
        return "design-only"
    return "ready"


def validate_components(
    data: Dict[str, Any],
    lifecycle: Dict[str, Dict[str, Any]],
    libraries: Dict[str, Dict[str, Any]],
    gaps: Dict[str, Dict[str, Any]],
    root: Path,
) -> Dict[str, Dict[str, Any]]:
    require(data.get("schemaVersion") == 1, "components: нужна schemaVersion 1")
    records = list(data.get("components") or []) + list(data.get("collections") or [])
    by_slug = unique_records(records, "slug", "components")
    sources: set[Tuple[str, str]] = set()
    for slug, record in by_slug.items():
        require_fields(record, {"name", "platform", "libraryId", "card", "source"}, f"component {slug}")
        platform = normalize_platform(record["platform"])
        library_id = record["libraryId"]
        require(library_id in libraries, f"component {slug}: неизвестная библиотека {library_id}")
        require(platform in libraries[library_id]["platforms"], f"component {slug}: платформа не совпадает с {library_id}")
        source = record["source"]
        require_fields(source, {"apiFileKey", "nodeId", "url"}, f"component {slug} source")
        identity = (str(source["apiFileKey"]), str(source["nodeId"]))
        require(identity not in sources, f"component {slug}: дублирующийся Figma source {identity}")
        sources.add(identity)
        require((root / DS / "components" / record["card"]).exists(), f"component {slug}: не найдена карточка {record['card']}")
        status = component_status(record)
        require(status in lifecycle, f"component {slug}: неизвестный lifecycle `{status}`")
        metadata = record.get("lifecycle") or {}
        if status == "planned":
            target = metadata.get("targetQuarter")
            require(isinstance(target, str) and QUARTER_PATTERN.fullmatch(target), f"component {slug}: planned требует targetQuarter YYYY-QN")
        if status == "deprecated":
            replacement = metadata.get("replacementComponent")
            gap_id = metadata.get("gapId")
            require(bool(replacement) or bool(gap_id), f"component {slug}: deprecated требует replacementComponent или gapId")
            if replacement:
                require(replacement in by_slug, f"component {slug}: неизвестная замена {replacement}")
            if gap_id:
                require(gap_id in gaps, f"component {slug}: неизвестный gap {gap_id}")
    return by_slug


def validate_gaps(data: Dict[str, Any]) -> Dict[str, Dict[str, Any]]:
    require(data.get("schemaVersion") == 1, "gaps: нужна schemaVersion 1")
    records = data.get("gaps")
    require(isinstance(records, list), "gaps: gaps должен быть массивом")
    by_id = unique_records(records, "id", "gaps")
    for gap_id, record in by_id.items():
        require(ID_PATTERN.fullmatch(gap_id) is not None, f"gap: некорректный id {gap_id}")
        require_fields(record, {"status", "title", "question", "platforms", "componentIds", "sourceLinks"}, f"gap {gap_id}")
        require(record["status"] in {"open", "resolved"}, f"gap {gap_id}: неизвестный status")
        for platform in record["platforms"]:
            normalize_platform(platform)
        require(bool(record["sourceLinks"]), f"gap {gap_id}: нужен хотя бы один sourceLink")
        if record["status"] == "resolved":
            require(bool(record.get("resolution")), f"gap {gap_id}: resolved требует resolution")
    return by_id


def validate_cases(data: Dict[str, Any], components: Dict[str, Dict[str, Any]]) -> Dict[str, Dict[str, Any]]:
    require(data.get("schemaVersion") == 1, "cases: нужна schemaVersion 1")
    records = data.get("cases")
    require(isinstance(records, list), "cases: cases должен быть массивом")
    by_id = unique_records(records, "id", "cases")
    for case_id, record in by_id.items():
        require(ID_PATTERN.fullmatch(case_id) is not None, f"case: некорректный id {case_id}")
        require_fields(
            record,
            {"status", "title", "platforms", "deviceClasses", "componentIds", "situation", "decision", "constraints", "sourceLinks"},
            f"case {case_id}",
        )
        require(record["status"] in {"draft", "confirmed"}, f"case {case_id}: неизвестный status")
        for component_id in record["componentIds"]:
            require(component_id in components, f"case {case_id}: неизвестный компонент {component_id}")
        for platform in record["platforms"]:
            normalize_platform(platform)
        require(bool(record["sourceLinks"]), f"case {case_id}: нужен хотя бы один sourceLink")
    return by_id


def validate_mappings(data: Dict[str, Any], components: Dict[str, Dict[str, Any]]) -> Dict[str, Dict[str, Any]]:
    require(data.get("schemaVersion") == 1, "mappings: нужна schemaVersion 1")
    platforms = set(data.get("platforms") or [])
    require(platforms == {"android", "ios", "web"}, "mappings: platforms должны быть android, ios, web")
    device_classes = set(data.get("deviceClasses") or [])
    require(device_classes == {"phone", "tablet"}, "mappings: deviceClasses должны быть phone, tablet")
    routes = data.get("supportedRoutes") or []
    actual_routes = {(item.get("sourcePlatform"), item.get("targetPlatform")) for item in routes}
    expected_routes = {(source, target) for source in platforms for target in platforms if source != target}
    require(actual_routes == expected_routes, "mappings: нужны все шесть направлений между android, ios и web")
    for route in routes:
        require(set(route.get("deviceClasses") or []) == device_classes, "mappings: каждый route должен поддерживать phone и tablet")
    records = data.get("mappings")
    require(isinstance(records, list), "mappings: mappings должен быть массивом")
    by_id = unique_records(records, "id", "mappings")
    for mapping_id, record in by_id.items():
        require(ID_PATTERN.fullmatch(mapping_id) is not None, f"mapping: некорректный id {mapping_id}")
        require_fields(
            record,
            {"status", "sourceComponent", "targetComponent", "sourcePlatform", "targetPlatform", "deviceClass", "propertyMappings", "variantMappings", "layoutRules", "navigationRules", "evidenceLinks"},
            f"mapping {mapping_id}",
        )
        require(record["status"] in {"candidate", "confirmed"}, f"mapping {mapping_id}: неизвестный status")
        require(record["sourceComponent"] in components, f"mapping {mapping_id}: неизвестный sourceComponent")
        require(record["targetComponent"] in components, f"mapping {mapping_id}: неизвестный targetComponent")
        source_platform = normalize_platform(record["sourcePlatform"])
        target_platform = normalize_platform(record["targetPlatform"])
        require((source_platform, target_platform) in expected_routes, f"mapping {mapping_id}: route не поддерживается")
        require(record["deviceClass"] in device_classes, f"mapping {mapping_id}: неизвестный deviceClass")
        require(normalize_platform(components[record["sourceComponent"]]["platform"]) == source_platform, f"mapping {mapping_id}: sourcePlatform не совпадает с компонентом")
        require(normalize_platform(components[record["targetComponent"]]["platform"]) == target_platform, f"mapping {mapping_id}: targetPlatform не совпадает с компонентом")
        if record["status"] == "confirmed":
            require(bool(record.get("confirmedBy")), f"mapping {mapping_id}: confirmed требует confirmedBy")
            require(bool(record["evidenceLinks"]), f"mapping {mapping_id}: confirmed требует evidenceLinks")
    return by_id


def read_sources(root: Path) -> Dict[str, Dict[str, Any]]:
    return {name: load_json(root / path) for name, path in PATHS.items() if name not in {"index", "context"}}


def validate_all(root: Path) -> Dict[str, Any]:
    data = read_sources(root)
    lifecycle = validate_lifecycle(data["lifecycle"])
    libraries = validate_libraries(data["libraries"])
    gaps = validate_gaps(data["gaps"])
    components = validate_components(data["components"], lifecycle, libraries, gaps, root)
    cases = validate_cases(data["cases"], components)
    mappings = validate_mappings(data["mappings"], components)
    for gap_id, gap in gaps.items():
        for component_id in gap["componentIds"]:
            require(component_id in components, f"gap {gap_id}: неизвестный компонент {component_id}")
    return {
        "data": data,
        "lifecycle": lifecycle,
        "libraries": libraries,
        "components": components,
        "cases": cases,
        "gaps": gaps,
        "mappings": mappings,
    }


def compact_component(record: Dict[str, Any], lifecycle: Dict[str, Dict[str, Any]], libraries: Dict[str, Dict[str, Any]]) -> Dict[str, Any]:
    status = component_status(record)
    source = record["source"]
    return {
        "id": record["slug"],
        "name": record["name"],
        "kind": record.get("kind", "component"),
        "platform": normalize_platform(record["platform"]),
        "deviceClasses": record.get("deviceClasses") or libraries[record["libraryId"]]["deviceClasses"],
        "libraryId": record["libraryId"],
        "lifecycle": status,
        "automaticUse": lifecycle[status]["automaticUse"],
        "card": f"design-system/components/{record['card']}",
        "figma": {
            "url": source["url"],
            "fileKey": source["fileKey"],
            "nodeId": source["nodeId"],
        },
        "lastCheckedAt": record.get("lastCheckedAt"),
    }


def build_index(validated: Dict[str, Any]) -> Dict[str, Any]:
    data = validated["data"]
    components = [
        compact_component(record, validated["lifecycle"], validated["libraries"])
        for _, record in sorted(validated["components"].items())
    ]
    return {
        "schemaVersion": 1,
        "sources": {
            "components": str(PATHS["components"]),
            "libraries": str(PATHS["libraries"]),
            "lifecycle": str(PATHS["lifecycle"]),
            "mappings": str(PATHS["mappings"]),
            "cases": str(PATHS["cases"]),
            "gaps": str(PATHS["gaps"]),
            "platformRules": "design-system/platforms",
            "tokenSnapshots": "design-system/tokens"
        },
        "lifecycle": data["lifecycle"],
        "libraries": data["libraries"]["libraries"],
        "components": components,
        "supportedRoutes": data["mappings"]["supportedRoutes"],
        "confirmedMappings": [item for item in data["mappings"]["mappings"] if item["status"] == "confirmed"],
        "confirmedCases": [item for item in data["cases"]["cases"] if item["status"] == "confirmed"],
        "openGaps": [item for item in data["gaps"]["gaps"] if item["status"] == "open"]
    }


def markdown_cell(value: Any) -> str:
    return str(value if value not in (None, "") else "—").replace("|", "\\|").replace("\n", " ")


def render_context(index: Dict[str, Any]) -> str:
    lines = [
        "# Okko DS agent context",
        "",
        "> Сгенерировано из `design-system/`. Не редактировать вручную.",
        "",
        "## Lifecycle",
        "",
        "| Статус | Маркер | Автоматическое использование | Значение |",
        "|---|---|---|---|",
    ]
    for status in index["lifecycle"]["statuses"]:
        lines.append(
            f"| `{status['id']}` | {status['marker']} | "
            f"{'да' if status['automaticUse'] else 'нет'} | {markdown_cell(status['description'])} |"
        )
    lines.extend([
        "",
        "## Библиотеки",
        "",
        "| ID | Название | Платформы | Статус | Зависимости |",
        "|---|---|---|---|---|",
    ])
    for library in index["libraries"]:
        lines.append(
            f"| `{library['id']}` | {markdown_cell(library['name'])} | "
            f"{', '.join(library['platforms'])} | `{library['status']}` | "
            f"{', '.join(library['dependencies']) or '—'} |"
        )
    lines.extend([
        "",
        "## Компоненты",
        "",
        "| Компонент | Платформа | Библиотека | Lifecycle | Карточка | Figma |",
        "|---|---|---|---|---|---|",
    ])
    for component in index["components"]:
        lines.append(
            f"| `{markdown_cell(component['name'])}` | `{component['platform']}` | "
            f"`{component['libraryId']}` | `{component['lifecycle']}` | "
            f"[`{component['id']}`](../components/{component['id']}.md) | "
            f"[node]({component['figma']['url']}) |"
        )
    lines.extend(["", "## Подтверждённые платформенные mappings", ""])
    if index["confirmedMappings"]:
        for mapping in index["confirmedMappings"]:
            lines.append(
                f"- `{mapping['sourceComponent']}` ({mapping['sourcePlatform']}) → "
                f"`{mapping['targetComponent']}` ({mapping['targetPlatform']}), "
                f"device `{mapping['deviceClass']}`."
            )
    else:
        lines.append("Подтверждённых mappings пока нет.")
    lines.extend(["", "## Подтверждённые кейсы", ""])
    if index["confirmedCases"]:
        for case in index["confirmedCases"]:
            lines.append(f"### {case['title']}")
            lines.extend(["", case["situation"], "", f"**Решение:** {case['decision']}", ""])
            for constraint in case["constraints"]:
                lines.append(f"- {constraint}")
    else:
        lines.append("Подтверждённых кейсов пока нет.")
    lines.extend(["", "## Открытые gaps", ""])
    if index["openGaps"]:
        for gap in index["openGaps"]:
            lines.append(f"- **{gap['title']}** — {gap['question']} (`{gap['id']}`)")
    else:
        lines.append("Открытых gaps пока нет.")
    lines.extend([
        "",
        "## Детальные источники",
        "",
        "- Платформенные правила: `design-system/platforms/`.",
        "- Snapshot токенов: `design-system/tokens/`; актуальные значения проверять в Tokens Studio Git.",
        "- Полные карточки компонентов: `design-system/components/`.",
        "",
    ])
    return "\n".join(lines)


def serialized_json(value: Dict[str, Any]) -> str:
    return json.dumps(value, ensure_ascii=False, indent=2) + "\n"


def expected_outputs(root: Path) -> Dict[Path, str]:
    validated = validate_all(root)
    index = build_index(validated)
    return {
        root / PATHS["index"]: serialized_json(index),
        root / PATHS["context"]: render_context(index),
    }


def write_atomic(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile("w", encoding="utf-8", dir=str(path.parent), delete=False) as handle:
        handle.write(content)
        temporary = Path(handle.name)
    temporary.replace(path)


def cmd_validate(args: argparse.Namespace) -> int:
    root = Path(args.root).resolve()
    validated = validate_all(root)
    print(
        "Каркас валиден: "
        f"{len(validated['libraries'])} библиотек, "
        f"{len(validated['components'])} компонентов/коллекций, "
        f"{len(validated['mappings'])} mappings, "
        f"{len(validated['cases'])} кейсов, "
        f"{len(validated['gaps'])} gaps"
    )
    return 0


def cmd_generate(args: argparse.Namespace) -> int:
    root = Path(args.root).resolve()
    outputs = expected_outputs(root)
    stale = [path for path, content in outputs.items() if not path.exists() or path.read_text(encoding="utf-8") != content]
    if args.check:
        if stale:
            raise KnowledgeError("Сгенерированный контекст устарел: " + ", ".join(str(path.relative_to(root)) for path in stale))
        print("Сгенерированный agent-контекст актуален")
        return 0
    for path, content in outputs.items():
        write_atomic(path, content)
    print("Сгенерированы: " + ", ".join(str(path.relative_to(root)) for path in outputs))
    return 0


def parser() -> argparse.ArgumentParser:
    result = argparse.ArgumentParser(description=__doc__)
    result.add_argument("--root", default=str(ROOT))
    subparsers = result.add_subparsers(dest="command", required=True)
    validate = subparsers.add_parser("validate")
    validate.set_defaults(func=cmd_validate)
    generate = subparsers.add_parser("generate")
    generate.add_argument("--check", action="store_true")
    generate.set_defaults(func=cmd_generate)
    return result


def main(argv: Optional[Sequence[str]] = None) -> int:
    try:
        args = parser().parse_args(argv)
        return args.func(args)
    except KnowledgeError as error:
        print(f"Ошибка: {error}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
