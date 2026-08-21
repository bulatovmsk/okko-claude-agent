#!/usr/bin/env python3
"""Register and refresh design-system components from Figma links.

The registry is persistent, while raw Figma responses remain in the ignored
`.figma-cache/` directory. Human-written card sections are never replaced:
only the block between FIGMA_SYNC markers is managed by this script.
"""

import argparse
import datetime as dt
import hashlib
import json
import re
import subprocess
import sys
import tempfile
import unicodedata
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Sequence, Tuple
from urllib.parse import parse_qs, unquote, urlparse


ROOT = Path(__file__).resolve().parents[1]
REGISTRY_PATH = Path("design-system/components/figma-sources.json")
LIBRARIES_MAP_PATH = Path(
    ".agents/skills/design-figma-libraries/references/libraries-map.md"
)
MANAGED_START = "<!-- FIGMA_SYNC:START -->"
MANAGED_END = "<!-- FIGMA_SYNC:END -->"
MAP_START = "<!-- FIGMA_COMPONENT_REGISTRY:START -->"
MAP_END = "<!-- FIGMA_COMPONENT_REGISTRY:END -->"
ALLOWED_NODE_TYPES = {"COMPONENT", "COMPONENT_SET"}


class ComponentError(RuntimeError):
    """A user-facing component workflow error."""


def normalize_node_id(value: str) -> str:
    decoded = unquote(value).strip()
    match = re.fullmatch(r"(\d+)(?:-|:)(\d+)", decoded)
    if not match:
        raise ComponentError(
            "node-id должен иметь формат 123-456 или 123:456"
        )
    return f"{match.group(1)}:{match.group(2)}"


def parse_figma_url(value: str) -> Dict[str, Optional[str]]:
    parsed = urlparse(value)
    host = (parsed.hostname or "").lower()
    if host != "figma.com" and not host.endswith(".figma.com"):
        raise ComponentError(f"Не Figma URL: {value}")

    parts = [unquote(part) for part in parsed.path.split("/") if part]
    if len(parts) < 2 or parts[0] not in {"design", "file"}:
        raise ComponentError(
            "Ожидается ссылка вида figma.com/design/<fileKey>/...?node-id=..."
        )

    file_key = parts[1]
    if not re.fullmatch(r"[A-Za-z0-9]+", file_key):
        raise ComponentError("Не удалось распознать fileKey в Figma URL")

    branch_key = None
    if "branch" in parts:
        index = parts.index("branch")
        if index + 1 >= len(parts):
            raise ComponentError("В Figma URL отсутствует branchKey после /branch/")
        branch_key = parts[index + 1]

    query = parse_qs(parsed.query)
    raw_node_ids = query.get("node-id") or query.get("node_id")
    if not raw_node_ids:
        raise ComponentError("В Figma URL отсутствует параметр node-id")
    node_id = normalize_node_id(raw_node_ids[0])

    return {
        "url": value,
        "fileKey": file_key,
        "branchKey": branch_key,
        "apiFileKey": branch_key or file_key,
        "nodeId": node_id,
    }


def status_from_name(name: str) -> str:
    lowered = name.lower()
    if name.startswith("🔴") or "[deprecated]" in lowered:
        return "deprecated"
    if name.startswith("🟡"):
        return "work-in-progress"
    if name.startswith("🟢"):
        return "ready"
    return "unknown"


def slugify(name: str, node_id: str) -> str:
    value = unicodedata.normalize("NFKD", name).encode("ascii", "ignore").decode()
    value = re.sub(r"[^a-zA-Z0-9]+", "-", value).strip("-").lower()
    return value or f"component-{node_id.replace(':', '-')}"


def walk_nodes(node: Dict[str, Any]) -> Iterable[Dict[str, Any]]:
    yield node
    for child in node.get("children") or []:
        yield from walk_nodes(child)


def variant_values(document: Dict[str, Any]) -> Dict[str, List[str]]:
    variants: Dict[str, set] = {}
    for child in document.get("children") or []:
        values = child.get("variantProperties") or {}
        if not values and child.get("type") == "COMPONENT":
            for part in child.get("name", "").split(","):
                if "=" in part:
                    key, value = part.split("=", 1)
                    values[key.strip()] = value.strip()
        for key, value in values.items():
            variants.setdefault(key, set()).add(str(value))
    return {key: sorted(values) for key, values in sorted(variants.items())}


def property_records(document: Dict[str, Any], variants: Dict[str, List[str]]) -> List[Dict[str, Any]]:
    records = []
    definitions = document.get("componentPropertyDefinitions") or {}
    for raw_name, definition in sorted(definitions.items()):
        name = str(definition.get("name") or re.sub(r"#\d+:\d+$", "", raw_name))
        record: Dict[str, Any] = {
            "name": name,
            "type": str(definition.get("type", "unknown")).lower(),
        }
        if name != raw_name:
            record["key"] = raw_name
        if "defaultValue" in definition:
            record["defaultValue"] = definition["defaultValue"]
        options = definition.get("variantOptions")
        if options:
            record["options"] = sorted(str(option) for option in options)
        elif name in variants:
            record["options"] = variants[name]
        records.append(record)

    known = {record["name"] for record in records}
    for name, options in variants.items():
        if name not in known:
            records.append({"name": name, "type": "variant", "options": options})
    return sorted(records, key=lambda record: record["name"].lower())


def dimension_records(document: Dict[str, Any]) -> List[Dict[str, Any]]:
    grouped: Dict[Tuple[float, float], Dict[str, Any]] = {}
    for child in document.get("children") or []:
        if child.get("type") != "COMPONENT":
            continue
        bounds = child.get("absoluteBoundingBox") or {}
        if "width" not in bounds or "height" not in bounds:
            continue
        key = (round(float(bounds["width"]), 2), round(float(bounds["height"]), 2))
        record = grouped.setdefault(
            key,
            {"width": key[0], "height": key[1], "count": 0, "examples": []},
        )
        record["count"] += 1
        if len(record["examples"]) < 3:
            record["examples"].append(child.get("name", ""))
    return [grouped[key] for key in sorted(grouped)]


def dependency_records(bundle: Dict[str, Any], document: Dict[str, Any]) -> List[Dict[str, str]]:
    component_meta = bundle.get("components") or {}
    dependencies: Dict[str, Dict[str, str]] = {}
    for node in walk_nodes(document):
        if node.get("type") != "INSTANCE" or not node.get("componentId"):
            continue
        node_id = str(node["componentId"])
        meta = component_meta.get(node_id) or {}
        record = {
            "nodeId": node_id,
            "name": str(meta.get("name") or node.get("name") or node_id),
        }
        component_set_id = meta.get("component_set_id") or meta.get("componentSetId")
        if component_set_id:
            record["componentSetId"] = str(component_set_id)
        dependencies[node_id] = record
    return sorted(dependencies.values(), key=lambda item: (item["name"].lower(), item["nodeId"]))


def extract_bundle(payload: Dict[str, Any], node_id: str) -> Dict[str, Any]:
    if "nodes" in payload:
        bundle = (payload.get("nodes") or {}).get(node_id)
        if not bundle:
            raise ComponentError(f"Figma не вернула node {node_id}")
        return bundle
    if "document" in payload:
        return payload
    if payload.get("type"):
        return {"document": payload}
    raise ComponentError("JSON не похож на ответ Figma nodes API")


def snapshot_from_payload(payload: Dict[str, Any], node_id: str) -> Dict[str, Any]:
    bundle = extract_bundle(payload, node_id)
    document = bundle.get("document") or {}
    variants = variant_values(document)
    return {
        "name": str(document.get("name") or ""),
        "nodeType": str(document.get("type") or ""),
        "description": str(document.get("description") or ""),
        "status": status_from_name(str(document.get("name") or "")),
        "properties": property_records(document, variants),
        "variants": variants,
        "variantCount": sum(
            1 for child in document.get("children") or [] if child.get("type") == "COMPONENT"
        ),
        "dimensions": dimension_records(document),
        "dependencies": dependency_records(bundle, document),
    }


def collection_snapshot_from_payload(payload: Dict[str, Any], node_id: str) -> Dict[str, Any]:
    bundle = extract_bundle(payload, node_id)
    document = bundle.get("document") or {}
    members = []
    for node in walk_nodes(document):
        if node.get("type") not in ALLOWED_NODE_TYPES:
            continue
        variants = variant_values(node)
        bounds = node.get("absoluteBoundingBox") or {}
        members.append(
            {
                "nodeId": str(node.get("id") or ""),
                "name": str(node.get("name") or ""),
                "nodeType": str(node.get("type") or ""),
                "status": status_from_name(str(node.get("name") or "")),
                "width": round(float(bounds["width"]), 2) if "width" in bounds else None,
                "height": round(float(bounds["height"]), 2) if "height" in bounds else None,
                "properties": property_records(node, variants),
                "dependencies": dependency_records(bundle, node),
            }
        )
    members.sort(key=lambda item: item["name"].lower())
    return {
        "name": str(document.get("name") or ""),
        "nodeType": str(document.get("type") or ""),
        "description": str(document.get("description") or ""),
        "status": "collection",
        "memberCount": len(members),
        "members": members,
    }


def snapshot_hash(snapshot: Dict[str, Any]) -> str:
    encoded = json.dumps(snapshot, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(encoded.encode("utf-8")).hexdigest()


def load_json(path: Path) -> Dict[str, Any]:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as error:
        raise ComponentError(f"Не найден JSON: {path}") from error
    except json.JSONDecodeError as error:
        raise ComponentError(f"Некорректный JSON {path}: {error}") from error


def fetch_payload(root: Path, source: Dict[str, Optional[str]]) -> Dict[str, Any]:
    path = f"/v1/files/{source['apiFileKey']}/nodes?ids={source['nodeId']}"
    process = subprocess.run(
        ["bash", str(root / "scripts/figma-api.sh"), path],
        cwd=str(root),
        capture_output=True,
        text=True,
    )
    if process.returncode:
        message = process.stderr.strip() or "Figma API вернул ошибку"
        raise ComponentError(message)
    try:
        return json.loads(process.stdout)
    except json.JSONDecodeError as error:
        raise ComponentError("Figma API вернул некорректный JSON") from error


def empty_registry() -> Dict[str, Any]:
    return {"schemaVersion": 1, "components": [], "collections": []}


def all_records(registry: Dict[str, Any]) -> List[Dict[str, Any]]:
    return list(registry.get("components") or []) + list(registry.get("collections") or [])


def load_registry(root: Path) -> Dict[str, Any]:
    path = root / REGISTRY_PATH
    if not path.exists():
        return empty_registry()
    registry = load_json(path)
    validate_registry_data(registry, root)
    return registry


def write_json_atomic(path: Path, value: Dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(
        "w", encoding="utf-8", dir=str(path.parent), delete=False
    ) as handle:
        json.dump(value, handle, ensure_ascii=False, indent=2)
        handle.write("\n")
        temporary = Path(handle.name)
    temporary.replace(path)


def now_iso() -> str:
    return dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def markdown_cell(value: Any) -> str:
    if isinstance(value, bool):
        text = "true" if value else "false"
    elif value is None:
        text = "—"
    else:
        text = str(value)
    return text.replace("|", "\\|").replace("\n", " ")


def source_link(source: Dict[str, Any], label: str = "Figma") -> str:
    return f"[{label}]({source['url']})"


def format_managed_block(record: Dict[str, Any]) -> str:
    if record.get("kind") == "collection":
        return format_collection_block(record)
    source = record["source"]
    snapshot = record["snapshot"]
    lines = [MANAGED_START, "## Актуальные данные Figma", ""]
    lines.append(
        f"> Последняя проверка: `{record['lastCheckedAt']}` · "
        f"структура `{record['snapshotHash'][:12]}` · статус `{snapshot['status']}`."
    )
    lines.extend(["", "### Свойства из компонента", ""])
    properties = snapshot.get("properties") or []
    if properties:
        lines.extend(["| Свойство | Тип | Значение по умолчанию | Варианты |", "|---|---|---|---|"])
        for prop in properties:
            options = " / ".join(prop.get("options") or []) or "—"
            lines.append(
                "| `{}` | `{}` | `{}` | {} |".format(
                    markdown_cell(prop["name"]),
                    markdown_cell(prop["type"]),
                    markdown_cell(prop.get("defaultValue")),
                    markdown_cell(options),
                )
            )
    else:
        lines.append("У ноды нет опубликованных component properties.")

    lines.extend(["", "### Варианты и размеры", ""])
    variants = snapshot.get("variants") or {}
    if variants:
        lines.extend(["| Ось | Значения |", "|---|---|"])
        for key, values in variants.items():
            lines.append(f"| `{markdown_cell(key)}` | {markdown_cell(' / '.join(values))} |")
        lines.append("")
    lines.append(f"Комбинаций в COMPONENT_SET: **{snapshot.get('variantCount', 0)}**.")

    dimensions = snapshot.get("dimensions") or []
    if dimensions:
        lines.extend(["", "| Размер | Количество вариантов | Примеры |", "|---|---:|---|"])
        for item in dimensions:
            examples = "; ".join(example for example in item.get("examples", []) if example)
            lines.append(
                f"| `{item['width']}×{item['height']}` | {item['count']} | {markdown_cell(examples or '—')} |"
            )

    state_axes = {
        key: values
        for key, values in variants.items()
        if any(marker in key.lower() for marker in ("state", "status", "selected", "interaction"))
    }
    if state_axes:
        lines.extend(["", "### Состояния", ""])
        for key, values in state_axes.items():
            lines.append(f"- `{markdown_cell(key)}`: {markdown_cell(' / '.join(values))}")

    lines.extend(["", "### Зависимости", ""])
    dependencies = snapshot.get("dependencies") or []
    if dependencies:
        for dependency in dependencies:
            suffix = f"; set `{dependency['componentSetId']}`" if dependency.get("componentSetId") else ""
            lines.append(f"- `{markdown_cell(dependency['name'])}` — node `{dependency['nodeId']}`{suffix}")
    else:
        lines.append("В Figma-ответе внешние component dependencies не найдены.")

    lines.extend(["", "### Источник", ""])
    lines.append(
        f"- {source_link(source, snapshot['name'] or record['name'])} — "
        f"fileKey `{source['fileKey']}`, "
        + (f"branchKey `{source['branchKey']}`, " if source.get("branchKey") else "")
        + f"API key `{source['apiFileKey']}`, node `{source['nodeId']}`, type `{snapshot['nodeType']}`."
    )
    for related in record.get("relatedSources") or []:
        related_snapshot = related.get("snapshot") or {}
        label = related_snapshot.get("name") or related.get("kind", "Источник")
        lines.append(
            f"- {source_link(related, label)} — `{related.get('kind', 'reference')}`, "
            f"node `{related['nodeId']}`."
        )
    lines.append(MANAGED_END)
    return "\n".join(lines)


def format_collection_block(record: Dict[str, Any]) -> str:
    source = record["source"]
    snapshot = record["snapshot"]
    lines = [MANAGED_START, "## Актуальные данные Figma", ""]
    lines.append(
        f"> Последняя проверка: `{record['lastCheckedAt']}` · "
        f"структура `{record['snapshotHash'][:12]}` · коллекция из "
        f"**{snapshot.get('memberCount', 0)}** компонентов."
    )
    lines.extend(
        [
            "",
            "### Layout-компоненты",
            "",
            "| Компонент | Размер | Свойства | nodeId |",
            "|---|---:|---|---|",
        ]
    )
    for member in snapshot.get("members") or []:
        width = member.get("width")
        height = member.get("height")
        size = f"{width:g}×{height:g}" if width is not None and height is not None else "—"
        properties = ", ".join(prop["name"] for prop in member.get("properties") or []) or "—"
        member_url = source["url"].split("?", 1)[0] + "?node-id=" + member["nodeId"].replace(":", "-")
        lines.append(
            f"| [{markdown_cell(member['name'])}]({member_url}) | `{size}` | "
            f"{markdown_cell(properties)} | `{member['nodeId']}` |"
        )

    dependency_names = sorted(
        {
            dependency["name"]
            for member in snapshot.get("members") or []
            for dependency in member.get("dependencies") or []
        }
    )
    lines.extend(["", "### Встроенные элементы", ""])
    if dependency_names:
        for name in dependency_names:
            lines.append(f"- `{markdown_cell(name)}`")
    else:
        lines.append("В Figma-ответе component dependencies не найдены.")

    lines.extend(["", "### Источники", ""])
    lines.append(
        f"- {source_link(source, snapshot['name'] or record['name'])} — "
        f"fileKey `{source['fileKey']}`, API key `{source['apiFileKey']}`, "
        f"node `{source['nodeId']}`, type `{snapshot['nodeType']}`."
    )
    for related in record.get("relatedSources") or []:
        related_snapshot = related.get("snapshot") or {}
        label = related_snapshot.get("name") or related.get("name") or related.get("kind", "Источник")
        lines.append(
            f"- {source_link(related, label)} — `{related.get('kind', 'reference')}`, "
            f"node `{related['nodeId']}`."
        )
    lines.append(MANAGED_END)
    return "\n".join(lines)


def replace_managed_block(text: str, block: str) -> str:
    pattern = re.compile(
        re.escape(MANAGED_START) + r".*?" + re.escape(MANAGED_END), re.DOTALL
    )
    if pattern.search(text):
        return pattern.sub(block, text).rstrip() + "\n"
    return text.rstrip() + "\n\n" + block + "\n"


def new_card(record: Dict[str, Any]) -> str:
    name = record["name"]
    description = (record.get("snapshot") or {}).get("description") or (
        "TODO: описать назначение после изучения продуктовых сценариев компонента."
    )
    sections = [
        f"# {name}",
        "",
        "## Назначение",
        "",
        description,
        "",
        "## Когда использовать",
        "",
        "- TODO: зафиксировать подтверждённые сценарии применения.",
        "",
        "## Когда НЕ использовать",
        "",
        "- TODO: указать ближайшие альтернативы из дизайн-системы.",
        "",
        "## Платформенные особенности iOS",
        "",
        "- TODO: проверить поведение, hit-area, VoiceOver и адаптацию iPhone/iPad.",
        "",
        "## Связанные компоненты",
        "",
        "- TODO: заполнить по зависимостям и продуктовым сценариям.",
        "",
        format_managed_block(record),
        "",
    ]
    return "\n".join(sections)


def source_identity(source: Dict[str, Any]) -> Tuple[str, str]:
    return str(source["apiFileKey"]), str(source["nodeId"])


def find_component(registry: Dict[str, Any], slug: str) -> Dict[str, Any]:
    for record in all_records(registry):
        if record.get("slug") == slug:
            return record
    raise ComponentError(f"Компонент не зарегистрирован: {slug}")


def find_source(registry: Dict[str, Any], source: Dict[str, Any]) -> Tuple[Dict[str, Any], Dict[str, Any]]:
    identity = source_identity(source)
    for record in all_records(registry):
        if source_identity(record["source"]) == identity:
            return record, record["source"]
        for related in record.get("relatedSources") or []:
            if source_identity(related) == identity:
                return record, related
    raise ComponentError(
        f"Источник не зарегистрирован: {source['apiFileKey']} / {source['nodeId']}"
    )


def snapshot_changes(before: Optional[Dict[str, Any]], after: Dict[str, Any]) -> List[str]:
    if before is None:
        return ["new"]
    changes = []
    for key, label in (
        ("name", "name"),
        ("nodeType", "node type"),
        ("status", "status"),
        ("variantCount", "variant count"),
    ):
        if before.get(key) != after.get(key):
            changes.append(f"{label}: {before.get(key)!r} → {after.get(key)!r}")
    if before.get("description") != after.get("description"):
        changes.append("description changed")

    before_members = {item["nodeId"]: item for item in before.get("members") or []}
    after_members = {item["nodeId"]: item for item in after.get("members") or []}
    if before_members or after_members:
        for member_id in sorted(after_members.keys() - before_members.keys()):
            changes.append(f"member added: {after_members[member_id]['name']} ({member_id})")
        for member_id in sorted(before_members.keys() - after_members.keys()):
            changes.append(f"member removed: {before_members[member_id]['name']} ({member_id})")
        for member_id in sorted(before_members.keys() & after_members.keys()):
            if before_members[member_id] != after_members[member_id]:
                changes.append(f"member changed: {after_members[member_id]['name']} ({member_id})")
        return changes

    before_properties = {
        item["name"]: item for item in before.get("properties") or []
    }
    after_properties = {
        item["name"]: item for item in after.get("properties") or []
    }
    for name in sorted(after_properties.keys() - before_properties.keys()):
        changes.append(f"property added: {name}")
    for name in sorted(before_properties.keys() - after_properties.keys()):
        changes.append(f"property removed: {name}")
    for name in sorted(before_properties.keys() & after_properties.keys()):
        if before_properties[name] != after_properties[name]:
            changes.append(f"property changed: {name}")

    before_variants = before.get("variants") or {}
    after_variants = after.get("variants") or {}
    for axis in sorted(after_variants.keys() - before_variants.keys()):
        changes.append(f"variant axis added: {axis}")
    for axis in sorted(before_variants.keys() - after_variants.keys()):
        changes.append(f"variant axis removed: {axis}")
    for axis in sorted(before_variants.keys() & after_variants.keys()):
        removed = sorted(set(before_variants[axis]) - set(after_variants[axis]))
        added = sorted(set(after_variants[axis]) - set(before_variants[axis]))
        if added or removed:
            parts = []
            if added:
                parts.append("+" + ", ".join(added))
            if removed:
                parts.append("-" + ", ".join(removed))
            changes.append(f"variant {axis}: {'; '.join(parts)}")

    if before.get("dimensions") != after.get("dimensions"):
        changes.append("dimensions changed")

    before_dependencies = {
        item["nodeId"]: item for item in before.get("dependencies") or []
    }
    after_dependencies = {
        item["nodeId"]: item for item in after.get("dependencies") or []
    }
    for node_id in sorted(after_dependencies.keys() - before_dependencies.keys()):
        changes.append(f"dependency added: {after_dependencies[node_id]['name']} ({node_id})")
    for node_id in sorted(before_dependencies.keys() - after_dependencies.keys()):
        changes.append(f"dependency removed: {before_dependencies[node_id]['name']} ({node_id})")
    for node_id in sorted(before_dependencies.keys() & after_dependencies.keys()):
        if before_dependencies[node_id] != after_dependencies[node_id]:
            changes.append(f"dependency changed: {node_id}")
    return changes


def upsert_component(
    registry: Dict[str, Any],
    source: Dict[str, Any],
    snapshot: Dict[str, Any],
    slug: Optional[str] = None,
    name: Optional[str] = None,
) -> Tuple[Dict[str, Any], List[str]]:
    if snapshot["nodeType"] not in ALLOWED_NODE_TYPES:
        raise ComponentError(
            f"Нода `{snapshot['name']}` имеет type `{snapshot['nodeType']}`. "
            "Для основной карточки нужна COMPONENT или COMPONENT_SET; "
            "гайд/продуктовый пример регистрируй как связанный источник."
        )
    identity = source_identity(source)
    existing = next(
        (
            item
            for item in registry.get("components") or []
            if source_identity(item["source"]) == identity
        ),
        None,
    )
    if existing is None and slug:
        existing = next(
            (item for item in registry.get("components") or [] if item.get("slug") == slug),
            None,
        )
    selected_slug = slug or (existing or {}).get("slug") or slugify(snapshot["name"], source["nodeId"])
    duplicate = next(
        (
            item
            for item in registry.get("components") or []
            if item.get("slug") == selected_slug and item is not existing
        ),
        None,
    )
    if duplicate:
        raise ComponentError(f"Slug уже занят: {selected_slug}")

    changes = snapshot_changes((existing or {}).get("snapshot"), snapshot)
    checked_at = now_iso()
    record = existing or {"slug": selected_slug, "platform": "iOS", "relatedSources": []}
    record.update(
        {
            "slug": selected_slug,
            "name": name or snapshot["name"],
            "card": f"{selected_slug}.md",
            "source": source,
            "lastCheckedAt": checked_at,
            "snapshotHash": snapshot_hash(snapshot),
            "snapshot": snapshot,
        }
    )
    if existing is None:
        registry.setdefault("components", []).append(record)
    registry["components"] = sorted(
        registry.get("components") or [], key=lambda item: item["slug"]
    )
    return record, changes


def upsert_collection(
    registry: Dict[str, Any],
    source: Dict[str, Any],
    snapshot: Dict[str, Any],
    slug: Optional[str] = None,
    name: Optional[str] = None,
) -> Tuple[Dict[str, Any], List[str]]:
    identity = source_identity(source)
    existing = next(
        (
            item
            for item in registry.get("collections") or []
            if source_identity(item["source"]) == identity
        ),
        None,
    )
    if existing is None and slug:
        existing = next(
            (item for item in registry.get("collections") or [] if item.get("slug") == slug),
            None,
        )
    selected_slug = slug or (existing or {}).get("slug") or slugify(snapshot["name"], source["nodeId"])
    if any(item.get("slug") == selected_slug and item is not existing for item in all_records(registry)):
        raise ComponentError(f"Slug уже занят: {selected_slug}")
    changes = snapshot_changes((existing or {}).get("snapshot"), snapshot)
    record = existing or {
        "kind": "collection",
        "slug": selected_slug,
        "platform": "iOS",
        "relatedSources": [],
    }
    record.update(
        {
            "kind": "collection",
            "slug": selected_slug,
            "name": name or snapshot["name"],
            "card": f"{selected_slug}.md",
            "source": source,
            "lastCheckedAt": now_iso(),
            "snapshotHash": snapshot_hash(snapshot),
            "snapshot": snapshot,
        }
    )
    if existing is None:
        registry.setdefault("collections", []).append(record)
    registry["collections"] = sorted(
        registry.get("collections") or [], key=lambda item: item["slug"]
    )
    return record, changes


def upsert_related_source(
    record: Dict[str, Any],
    source: Dict[str, Any],
    snapshot: Dict[str, Any],
    kind: str,
) -> List[str]:
    existing = next(
        (
            item
            for item in record.get("relatedSources") or []
            if source_identity(item) == source_identity(source)
        ),
        None,
    )
    changes = snapshot_changes((existing or {}).get("snapshot"), snapshot)
    target = existing or source.copy()
    target.update(
        {
            "kind": kind,
            "lastCheckedAt": now_iso(),
            "snapshotHash": snapshot_hash(snapshot),
            "snapshot": snapshot,
        }
    )
    if existing is None:
        record.setdefault("relatedSources", []).append(target)
    record["relatedSources"] = sorted(
        record.get("relatedSources") or [], key=lambda item: (item["kind"], item["nodeId"])
    )
    return changes


def write_card(root: Path, record: Dict[str, Any]) -> None:
    path = root / "design-system/components" / record["card"]
    if path.exists():
        content = replace_managed_block(path.read_text(encoding="utf-8"), format_managed_block(record))
    else:
        content = new_card(record)
    path.write_text(content, encoding="utf-8")


def render_registry_table(registry: Dict[str, Any]) -> str:
    lines = [
        MAP_START,
        "| Компонент | API fileKey | nodeId | Статус | Карточка | Проверено |",
        "|---|---|---|---|---|---|",
    ]
    for record in registry.get("components") or []:
        source = record["source"]
        snapshot = record.get("snapshot") or {}
        lines.append(
            f"| {source_link(source, record['name'])} | `{source['apiFileKey']}` | "
            f"`{source['nodeId']}` | `{snapshot.get('status', 'unknown')}` | "
            f"[`{record['card']}`](../../../../design-system/components/{record['card']}) | "
            f"`{record.get('lastCheckedAt', 'not checked')}` |"
        )
    for record in registry.get("collections") or []:
        source = record["source"]
        snapshot = record.get("snapshot") or {}
        lines.append(
            f"| {source_link(source, record['name'])} | `{source['apiFileKey']}` | "
            f"`{source['nodeId']}` | `collection ({snapshot.get('memberCount', 0)})` | "
            f"[`{record['card']}`](../../../../design-system/components/{record['card']}) | "
            f"`{record.get('lastCheckedAt', 'not checked')}` |"
        )
    lines.append(MAP_END)
    return "\n".join(lines)


def update_libraries_map(root: Path, registry: Dict[str, Any]) -> None:
    path = root / LIBRARIES_MAP_PATH
    text = path.read_text(encoding="utf-8")
    block = render_registry_table(registry)
    pattern = re.compile(re.escape(MAP_START) + r".*?" + re.escape(MAP_END), re.DOTALL)
    if pattern.search(text):
        updated = pattern.sub(block, text)
    else:
        anchor = "## Продуктовые файлы"
        section = (
            "## Машиночитаемый реестр iOS-компонентов\n\n"
            "Блок генерируется из `design-system/components/figma-sources.json`.\n\n"
            + block
            + "\n\n"
        )
        if anchor in text:
            updated = text.replace(anchor, section + anchor, 1)
        else:
            updated = text.rstrip() + "\n\n" + section
    path.write_text(updated, encoding="utf-8")


def validate_registry_data(registry: Dict[str, Any], root: Optional[Path] = None) -> None:
    if registry.get("schemaVersion") != 1:
        raise ComponentError("Неподдерживаемая schemaVersion реестра компонентов")
    slugs = set()
    identities = set()
    for record in all_records(registry):
        required = {"slug", "name", "platform", "card", "source"}
        missing = required - set(record)
        if missing:
            raise ComponentError(f"В записи компонента отсутствуют поля: {sorted(missing)}")
        if record["slug"] in slugs:
            raise ComponentError(f"Дублирующийся slug: {record['slug']}")
        slugs.add(record["slug"])
        identity = source_identity(record["source"])
        if identity in identities:
            raise ComponentError(f"Дублирующийся Figma source: {identity}")
        identities.add(identity)
        if normalize_node_id(record["source"]["nodeId"]) != record["source"]["nodeId"]:
            raise ComponentError(f"nodeId не нормализован: {record['source']['nodeId']}")
        if root is not None and not (root / "design-system/components" / record["card"]).exists():
            raise ComponentError(f"Не найдена карточка: {record['card']}")
        for related in record.get("relatedSources") or []:
            related_identity = source_identity(related)
            if related_identity in identities:
                raise ComponentError(f"Дублирующийся Figma source: {related_identity}")
            identities.add(related_identity)
        if record.get("kind") == "collection":
            member_ids = set()
            for member in (record.get("snapshot") or {}).get("members") or []:
                member_id = normalize_node_id(member["nodeId"])
                if member_id in member_ids:
                    raise ComponentError(f"Дублирующийся member nodeId: {member_id}")
                member_ids.add(member_id)


def validate_markdown_links(root: Path) -> None:
    component_dir = root / "design-system/components"
    link_pattern = re.compile(r"\[[^\]]+\]\(([^)]+\.md)(?:#[^)]+)?\)")
    missing = []
    for path in component_dir.glob("*.md"):
        for target in link_pattern.findall(path.read_text(encoding="utf-8")):
            if "://" in target:
                continue
            resolved = (path.parent / target).resolve()
            if not resolved.exists():
                missing.append(f"{path.name} → {target}")
    if missing:
        raise ComponentError("Неразрешённые Markdown-ссылки: " + ", ".join(missing))


def persist(root: Path, registry: Dict[str, Any], changed_records: Sequence[Dict[str, Any]]) -> None:
    for record in changed_records:
        write_card(root, record)
    write_json_atomic(root / REGISTRY_PATH, registry)
    update_libraries_map(root, registry)


def finalize(root: Path) -> None:
    for script in ("sync-skill-references.sh", "validate-skills.sh"):
        subprocess.run(["bash", str(root / "scripts" / script)], cwd=str(root), check=True)


def payload_for(args: argparse.Namespace, root: Path, source: Dict[str, Any]) -> Dict[str, Any]:
    if args.payload:
        return load_json(Path(args.payload).resolve())
    return fetch_payload(root, source)


def cmd_parse(args: argparse.Namespace) -> int:
    parsed = [parse_figma_url(value) for value in args.urls]
    print(json.dumps(parsed, ensure_ascii=False, indent=2))
    return 0


def cmd_register(args: argparse.Namespace) -> int:
    if args.slug and len(args.urls) != 1:
        raise ComponentError("--slug можно использовать только с одной ссылкой")
    if args.payload and len(args.urls) != 1:
        raise ComponentError("--payload можно использовать только с одной ссылкой")
    if args.kind not in {"component", "collection"} and not args.component:
        raise ComponentError("Для guide/product/example укажи --component <slug>")

    root = Path(args.root).resolve()
    registry = load_registry(root)
    changed_records: List[Dict[str, Any]] = []
    reports = []
    for url in args.urls:
        source = parse_figma_url(url)
        payload = payload_for(args, root, source)
        snapshot = (
            collection_snapshot_from_payload(payload, source["nodeId"])
            if args.kind == "collection"
            else snapshot_from_payload(payload, source["nodeId"])
        )
        if args.kind == "component":
            record, changes = upsert_component(
                registry, source, snapshot, slug=args.slug, name=args.name
            )
        elif args.kind == "collection":
            record, changes = upsert_collection(
                registry, source, snapshot, slug=args.slug, name=args.name
            )
        else:
            record = find_component(registry, args.component)
            changes = upsert_related_source(record, source, snapshot, args.kind)
        changed_records.append(record)
        reports.append({"component": record["slug"], "source": source, "changes": changes})

    if not args.dry_run:
        persist(root, registry, changed_records)
        validate_registry_data(registry, root)
        validate_markdown_links(root)
        if not args.no_sync:
            finalize(root)
    print(json.dumps(reports, ensure_ascii=False, indent=2))
    return 0


def cmd_refresh(args: argparse.Namespace) -> int:
    root = Path(args.root).resolve()
    registry = load_registry(root)
    targets: List[Tuple[Dict[str, Any], Dict[str, Any]]] = []
    if not args.targets:
        targets = [(record, record["source"]) for record in all_records(registry)]
    else:
        for target in args.targets:
            if target.startswith("http://") or target.startswith("https://"):
                targets.append(find_source(registry, parse_figma_url(target)))
            else:
                record = find_component(registry, target)
                targets.append((record, record["source"]))
    if args.payload and len(targets) != 1:
        raise ComponentError("--payload можно использовать только с одним target")

    reports = []
    changed_records: List[Dict[str, Any]] = []
    for record, source in targets:
        payload = payload_for(args, root, source)
        snapshot = (
            collection_snapshot_from_payload(payload, source["nodeId"])
            if record.get("kind") == "collection" and source is record["source"]
            else snapshot_from_payload(payload, source["nodeId"])
        )
        if source is record["source"]:
            if record.get("kind") == "collection":
                updated, changes = upsert_collection(
                    registry, source, snapshot, slug=record["slug"], name=record["name"]
                )
            else:
                updated, changes = upsert_component(
                    registry, source, snapshot, slug=record["slug"], name=record["name"]
                )
            record = updated
        else:
            changes = upsert_related_source(record, source, snapshot, source["kind"])
        changed_records.append(record)
        reports.append({"component": record["slug"], "source": source, "changes": changes})

    if not args.dry_run:
        persist(root, registry, changed_records)
        validate_registry_data(registry, root)
        validate_markdown_links(root)
        if not args.no_sync:
            finalize(root)
    print(json.dumps(reports, ensure_ascii=False, indent=2))
    return 0


def cmd_validate(args: argparse.Namespace) -> int:
    root = Path(args.root).resolve()
    registry = load_registry(root)
    validate_registry_data(registry, root)
    validate_markdown_links(root)
    print(
        f"Реестр валиден: {len(registry['components'])} компонентов, "
        f"{len(registry.get('collections') or [])} коллекций"
    )
    return 0


def parser() -> argparse.ArgumentParser:
    common = argparse.ArgumentParser(add_help=False)
    common.add_argument("--root", default=str(ROOT), help=argparse.SUPPRESS)

    result = argparse.ArgumentParser(description=__doc__)
    subparsers = result.add_subparsers(dest="command", required=True)

    parse_command = subparsers.add_parser("parse", parents=[common], help="Нормализовать Figma URL")
    parse_command.add_argument("urls", nargs="+")
    parse_command.set_defaults(func=cmd_parse)

    register = subparsers.add_parser("register", parents=[common], help="Зарегистрировать источник")
    register.add_argument("urls", nargs="+")
    register.add_argument(
        "--kind",
        choices=["component", "collection", "guide", "product", "example"],
        default="component",
    )
    register.add_argument("--component", help="Slug основной карточки для связанного источника")
    register.add_argument("--slug")
    register.add_argument("--name")
    register.add_argument("--payload", help="Локальный JSON вместо REST-запроса")
    register.add_argument("--dry-run", action="store_true")
    register.add_argument("--no-sync", action="store_true", help="Не пересобирать references и не валидировать skills")
    register.set_defaults(func=cmd_register)

    refresh = subparsers.add_parser("refresh", parents=[common], help="Актуализировать зарегистрированные источники")
    refresh.add_argument("targets", nargs="*", help="Slug или сохранённая Figma-ссылка; без target обновляются все")
    refresh.add_argument("--payload", help="Локальный JSON вместо REST-запроса")
    refresh.add_argument("--dry-run", action="store_true")
    refresh.add_argument("--no-sync", action="store_true", help="Не пересобирать references и не валидировать skills")
    refresh.set_defaults(func=cmd_refresh)

    validate = subparsers.add_parser("validate", parents=[common], help="Проверить реестр и локальные ссылки")
    validate.set_defaults(func=cmd_validate)
    return result


def main(argv: Optional[Sequence[str]] = None) -> int:
    try:
        args = parser().parse_args(argv)
        return args.func(args)
    except ComponentError as error:
        print(f"Ошибка: {error}", file=sys.stderr)
        return 2
    except subprocess.CalledProcessError as error:
        print(f"Ошибка проверки: {error}", file=sys.stderr)
        return error.returncode or 1


if __name__ == "__main__":
    raise SystemExit(main())
