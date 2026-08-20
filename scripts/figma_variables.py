#!/usr/bin/env python3
"""Resolve Figma variable aliases and write deterministic token tables."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any


TARGETS = {
    "colors": {
        "file": "tokens/colors.md",
        "mode": "Dark",
        "sections": (
            ("VARDEFS_FROM_MCP:semantic", ("color/", "color."), "Токен", "Значение", True),
            ("VARDEFS_FROM_MCP:brand", ("brand/", "brand."), "Токен", "Значение", True),
        ),
    },
    "spacing": {
        "file": "tokens/spacing.md",
        "mode": "Web&Mobile",
        "sections": (("VARDEFS_FROM_PLUGIN_API:spacing", ("spacing/", "screen-padding/"), "Токен", "Значение", False),),
    },
    "corner-radius": {
        "file": "tokens/corner-radius.md",
        "mode": "Web&Mobile",
        "sections": (("VARDEFS_FROM_PLUGIN_API:corner-radius", ("corner-radius/",), "Токен", "Значение", False),),
    },
    "spacing-tv": {
        "file": "tokens/spacing-tv.md",
        "mode": "TV",
        "sections": (("VARDEFS_FROM_PLUGIN_API:spacing-tv", ("spacing/", "screen-padding/"), "Токен", "Значение (px)", False),),
    },
    "corner-radius-tv": {
        "file": "tokens/corner-radius-tv.md",
        "mode": "TV",
        "sections": (
            ("VARDEFS_FROM_PLUGIN_API:corner-radius-tv", ("corner-radius/",), "Токен", "Значение (px)", False),
            ("VARDEFS_FROM_PLUGIN_API:corner-radius-tv-focus", ("corner-radius/focus/",), "Токен", "Значение (px)", False),
        ),
    },
}


class VariableError(RuntimeError):
    pass


def _as_map(value: Any) -> dict[str, dict[str, Any]]:
    if isinstance(value, dict):
        return value
    if isinstance(value, list):
        return {str(item["id"]): item for item in value}
    return {}


def _payload_maps(payload: dict[str, Any]) -> tuple[dict[str, dict[str, Any]], dict[str, dict[str, Any]]]:
    root = payload.get("meta", payload)
    variables = _as_map(root.get("variables", payload.get("variables", {})))
    collections = _as_map(root.get("variableCollections", root.get("collections", payload.get("collections", {}))))
    return variables, collections


def _is_alias(value: Any) -> bool:
    return isinstance(value, dict) and value.get("type") == "VARIABLE_ALIAS" and bool(value.get("id"))


def _mode_name(collection: dict[str, Any], mode_id: str) -> str | None:
    for mode in collection.get("modes", []):
        if str(mode.get("modeId")) == str(mode_id):
            return mode.get("name")
    return None


def _mode_id(collection: dict[str, Any], wanted: str | None) -> str | None:
    modes = collection.get("modes", [])
    if wanted:
        wanted_folded = wanted.casefold()
        for mode in modes:
            if str(mode.get("name", "")).casefold() == wanted_folded:
                return str(mode.get("modeId"))
    if len(modes) == 1:
        return str(modes[0].get("modeId"))
    return None


def resolve_payload(payload: dict[str, Any], mode_name: str | None = None) -> dict[str, Any]:
    """Return name -> resolved value for REST or compact Plugin API payloads."""
    variables, collections = _payload_maps(payload)

    # get_variable_defs-compatible input: {"token/name": value}
    if not variables:
        direct = payload.get("resolvedValues", payload)
        if isinstance(direct, dict) and all(not isinstance(v, dict) or "type" not in v for v in direct.values()):
            return direct
        raise VariableError("В JSON не найдены variables или resolvedValues")

    cache: dict[tuple[str, str], Any] = {}
    active: set[tuple[str, str]] = set()

    def resolve(variable_id: str, requested_mode: str | None, inherited_mode_name: str | None = None) -> Any:
        variable = variables.get(variable_id)
        if not variable:
            raise VariableError(f"Alias ссылается на неизвестную variable {variable_id}")
        collection = collections.get(str(variable.get("variableCollectionId")), {})
        selected_mode = requested_mode
        values = variable.get("valuesByMode", {})
        if selected_mode not in values:
            selected_mode = _mode_id(collection, inherited_mode_name or mode_name)
        if selected_mode not in values and len(values) == 1:
            selected_mode = str(next(iter(values)))
        if selected_mode not in values:
            raise VariableError(f"Не найден mode для {variable.get('name', variable_id)}")

        key = (variable_id, str(selected_mode))
        if key in cache:
            return cache[key]
        if key in active:
            raise VariableError(f"Циклический alias у {variable.get('name', variable_id)}")
        active.add(key)
        value = values[selected_mode]
        if _is_alias(value):
            current_mode_name = _mode_name(collection, str(selected_mode)) or inherited_mode_name or mode_name
            value = resolve(str(value["id"]), str(selected_mode), current_mode_name)
        active.remove(key)
        cache[key] = value
        return value

    result: dict[str, Any] = {}
    for variable_id, variable in variables.items():
        if variable.get("deletedButReferenced"):
            continue
        collection = collections.get(str(variable.get("variableCollectionId")), {})
        selected_mode = _mode_id(collection, mode_name)
        values = variable.get("valuesByMode", {})
        if selected_mode is None and len(values) == 1:
            selected_mode = str(next(iter(values)))
        if selected_mode is None:
            continue
        result[str(variable.get("name", variable_id))] = resolve(str(variable_id), selected_mode, mode_name)
    return result


def _natural_key(name: str) -> list[Any]:
    return [int(part) if part.isdigit() else part.casefold() for part in re.split(r"(\d+)", name)]


def _format_color(value: Any) -> str:
    if isinstance(value, str):
        return value.upper() if value.startswith("#") else value
    if isinstance(value, dict) and all(channel in value for channel in ("r", "g", "b")):
        channels = [round(float(value[channel]) * 255) for channel in ("r", "g", "b")]
        alpha = round(float(value.get("a", 1)) * 255)
        suffix = f"{alpha:02X}" if alpha < 255 else ""
        return "#" + "".join(f"{channel:02X}" for channel in channels) + suffix
    return str(value)


def _format_value(value: Any, color: bool) -> str:
    if color:
        return _format_color(value)
    if isinstance(value, float) and value.is_integer():
        return str(int(value))
    if isinstance(value, (str, int, float, bool)):
        return str(value)
    return json.dumps(value, ensure_ascii=False, sort_keys=True)


def _matches(name: str, prefixes: tuple[str, ...], marker: str) -> bool:
    normalized = name.casefold().replace(".", "/")
    if marker.endswith("corner-radius-tv") and "/focus/" in normalized:
        return False
    return any(normalized.startswith(prefix.casefold().replace(".", "/")) for prefix in prefixes)


def _display_name(name: str, target: str) -> str:
    if target in {"spacing", "corner-radius", "colors"}:
        return name.replace("/", ".")
    return name


def _render_table(values: dict[str, Any], prefixes: tuple[str, ...], left: str, right: str, color: bool, target: str, marker: str) -> tuple[str, int]:
    selected = [(name, value) for name, value in values.items() if _matches(name, prefixes, marker)]
    selected.sort(key=lambda item: _natural_key(item[0]))
    if not selected:
        raise VariableError(f"Для {marker} не найдено подходящих variables")
    lines = [f"| {left} | {right} |", "|---|---:|" if not color else "|---|---|"]
    for name, value in selected:
        lines.append(f"| `{_display_name(name, target)}` | `{_format_value(value, color)}` |")
    return "\n".join(lines), len(selected)


def apply_target(payload: dict[str, Any], design_system_dir: Path, target: str, mode_name: str | None = None) -> dict[str, Any]:
    config = TARGETS[target]
    effective_mode = mode_name or config["mode"]
    values = resolve_payload(payload, effective_mode)
    path = design_system_dir / str(config["file"])
    text = path.read_text()
    counts: dict[str, int] = {}
    for marker, prefixes, left, right, color in config["sections"]:
        table, count = _render_table(values, prefixes, left, right, color, target, marker)
        pattern = rf"<!--[ \t]*{re.escape(marker)}(?:[ \t]+—[^>]*)?[ \t]*-->"
        text, replacements = re.subn(pattern, table, text, count=1)
        if replacements != 1:
            raise VariableError(f"Маркер {marker} не найден в {path}")
        counts[marker] = count
    path.write_text(text)
    return {"target": target, "file": str(path), "mode": effective_mode, "variables": counts}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, type=Path)
    parser.add_argument("--design-system-dir", required=True, type=Path)
    parser.add_argument("--target", required=True, choices=sorted(TARGETS))
    parser.add_argument("--mode")
    args = parser.parse_args()

    payload = json.loads(args.input.read_text())
    result = apply_target(payload, args.design_system_dir, args.target, args.mode)
    print(json.dumps(result, ensure_ascii=False, sort_keys=True))


if __name__ == "__main__":
    main()
