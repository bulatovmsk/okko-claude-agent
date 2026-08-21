#!/usr/bin/env python3
"""Read-only access to the Okko Tokens Studio source-of-truth repository."""

from __future__ import annotations

import argparse
import fcntl
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable


REPOSITORY_URL = "https://github.com/bulatovmsk/token-studio-repo.git"
BRANCH = "main"
TOKENS_FOLDER = "themes"
REQUIRED_FILES = (
    "themes/$metadata.json",
    "themes/$themes.json",
    "themes/Primitives.json",
)


class TokenSourceError(RuntimeError):
    """Raised when the canonical token source cannot be read safely."""


@dataclass(frozen=True)
class TokenRecord:
    token_set: str
    path: str
    value: Any
    token_type: str | None

    def as_dict(self) -> dict[str, Any]:
        aliases = re.findall(r"\{([^{}]+)\}", self.value) if isinstance(self.value, str) else []
        return {
            "set": self.token_set,
            "file": f"{TOKENS_FOLDER}/{self.token_set}.json",
            "path": self.path,
            "value": self.value,
            "type": self.token_type,
            "aliases": aliases,
        }


def project_root() -> Path:
    for parent in Path(__file__).resolve().parents:
        if (parent / ".git").exists() and (parent / ".agents").is_dir():
            return parent
    return Path.cwd()


def cache_root() -> Path:
    configured = os.environ.get("TOKEN_STUDIO_CACHE_DIR")
    return Path(configured).expanduser().resolve() if configured else project_root() / ".token-studio-cache"


def run_git(args: list[str], cwd: Path | None = None) -> str:
    environment = os.environ.copy()
    environment["GIT_TERMINAL_PROMPT"] = "0"
    try:
        result = subprocess.run(
            ["git", *args],
            cwd=cwd,
            env=environment,
            check=True,
            capture_output=True,
            text=True,
            timeout=60,
        )
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired, OSError) as exc:
        detail = getattr(exc, "stderr", "") or str(exc)
        raise TokenSourceError(detail.strip()) from exc
    return result.stdout.strip()


def local_commit(repository: Path) -> str | None:
    if not (repository / ".git").is_dir():
        return None
    try:
        return run_git(["rev-parse", "HEAD"], cwd=repository)
    except TokenSourceError:
        return None


def remote_commit() -> str:
    output = run_git(["ls-remote", REPOSITORY_URL, f"refs/heads/{BRANCH}"])
    if not output:
        raise TokenSourceError(f"В удалённом репозитории не найдена ветка {BRANCH}")
    return output.split()[0]


def validate_repository(repository: Path) -> None:
    missing = [path for path in REQUIRED_FILES if not (repository / path).is_file()]
    if missing:
        raise TokenSourceError("В source of truth отсутствуют обязательные файлы: " + ", ".join(missing))

    json_files = sorted((repository / TOKENS_FOLDER).rglob("*.json"))
    if not json_files:
        raise TokenSourceError("В source of truth не найдены JSON-файлы токенов")
    for path in json_files:
        try:
            json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            raise TokenSourceError(f"Некорректный JSON: {path.relative_to(repository)}: {exc}") from exc


def clone_snapshot(destination: Path) -> None:
    run_git(
        [
            "clone",
            "--depth",
            "1",
            "--single-branch",
            "--branch",
            BRANCH,
            REPOSITORY_URL,
            str(destination),
        ]
    )
    ensure_read_only_remote(destination)
    validate_repository(destination)


def ensure_read_only_remote(repository: Path) -> None:
    fetch_url = run_git(["remote", "get-url", "origin"], cwd=repository)
    if fetch_url != REPOSITORY_URL:
        raise TokenSourceError(f"Неожиданный fetch URL локального кэша: {fetch_url}")
    # Even an accidental `git push` from the cache must fail locally.
    run_git(["remote", "set-url", "--push", "origin", "PUSH_DISABLED_READ_ONLY_CACHE"], cwd=repository)


def refresh_locked(root: Path) -> dict[str, Any]:
    repository = root / "repository"
    latest = remote_commit()
    current = local_commit(repository)

    if current == latest:
        ensure_read_only_remote(repository)
        validate_repository(repository)
        return {
            "fresh": True,
            "updated": False,
            "commit": current,
            "branch": BRANCH,
            "repository": REPOSITORY_URL,
            "cache": str(repository),
        }

    staging = Path(tempfile.mkdtemp(prefix="snapshot-", dir=root)) / "repository"
    previous = root / "repository.previous"
    try:
        clone_snapshot(staging)
        cloned = local_commit(staging)
        if not cloned:
            raise TokenSourceError("Не удалось определить commit загруженного source of truth")

        if previous.exists():
            shutil.rmtree(previous)
        if repository.exists():
            repository.rename(previous)
        staging.rename(repository)
        ensure_read_only_remote(repository)
        if previous.exists():
            shutil.rmtree(previous)
    except Exception:
        if not repository.exists() and previous.exists():
            previous.rename(repository)
        raise
    finally:
        staging_parent = staging.parent
        if staging_parent.exists():
            shutil.rmtree(staging_parent)

    return {
        "fresh": True,
        "updated": True,
        "commit": local_commit(repository),
        "branch": BRANCH,
        "repository": REPOSITORY_URL,
        "cache": str(repository),
    }


def refresh() -> dict[str, Any]:
    root = cache_root()
    root.mkdir(parents=True, exist_ok=True)
    with (root / "refresh.lock").open("a+", encoding="utf-8") as lock:
        fcntl.flock(lock, fcntl.LOCK_EX)
        return refresh_locked(root)


def cached_status() -> dict[str, Any]:
    repository = cache_root() / "repository"
    commit = local_commit(repository)
    return {
        "fresh": False,
        "updated": False,
        "commit": commit,
        "branch": BRANCH,
        "repository": REPOSITORY_URL,
        "cache": str(repository),
        "available": bool(commit),
    }


def token_json_files(repository: Path, include_archive: bool = False) -> Iterable[Path]:
    for path in sorted((repository / TOKENS_FOLDER).rglob("*.json")):
        relative = path.relative_to(repository / TOKENS_FOLDER)
        if path.name in {"$metadata.json", "$themes.json"}:
            continue
        if not include_archive and relative.parts[0] == "_archive":
            continue
        yield path


def flatten_tokens(
    node: Any,
    token_set: str,
    parts: tuple[str, ...] = (),
    inherited_type: str | None = None,
) -> Iterable[TokenRecord]:
    if not isinstance(node, dict):
        return

    group_type = node.get("$type", inherited_type)
    if "value" in node or "$value" in node:
        value_key = "value" if "value" in node else "$value"
        token_type = node.get("type") or node.get("$type") or inherited_type
        yield TokenRecord(token_set, ".".join(parts), node[value_key], token_type)
        return

    for key, value in node.items():
        if key in {"$description", "$extensions", "$type"}:
            continue
        yield from flatten_tokens(value, token_set, (*parts, key), group_type)


def load_records(repository: Path, include_archive: bool = False) -> list[TokenRecord]:
    records: list[TokenRecord] = []
    base = repository / TOKENS_FOLDER
    for path in token_json_files(repository, include_archive=include_archive):
        token_set = path.relative_to(base).with_suffix("").as_posix()
        data = json.loads(path.read_text(encoding="utf-8"))
        records.extend(flatten_tokens(data, token_set))
    return records


def selected_records(records: list[TokenRecord], query: str, exact: bool, token_set: str | None) -> list[TokenRecord]:
    needle = query.casefold()
    matches: list[TokenRecord] = []
    for record in records:
        if token_set and token_set.casefold() not in record.token_set.casefold():
            continue
        haystack = record.path.casefold() if exact else f"{record.token_set} {record.path}".casefold()
        if (haystack == needle) if exact else (needle in haystack):
            matches.append(record)
    return matches


def emit(payload: Any) -> None:
    json.dump(payload, sys.stdout, ensure_ascii=False, indent=2)
    sys.stdout.write("\n")


def main() -> int:
    parser = argparse.ArgumentParser(description="Read-only query of the Okko Tokens Studio source of truth")
    parser.add_argument("--offline", action="store_true", help="Use the existing cache without checking GitHub")
    parser.add_argument("--include-archive", action="store_true", help="Include archived token sets")
    subparsers = parser.add_subparsers(dest="command", required=True)

    subparsers.add_parser("refresh", help="Refresh and validate the local read-only snapshot")
    subparsers.add_parser("status", help="Show source and cached commit information")
    subparsers.add_parser("sets", help="List token sets")
    subparsers.add_parser("themes", help="List theme groups and selected token sets")

    for command in ("find", "get"):
        child = subparsers.add_parser(command)
        child.add_argument("query")
        child.add_argument("--set", dest="token_set", help="Limit results to a token-set path fragment")
        child.add_argument("--limit", type=int, default=100)

    args = parser.parse_args()

    try:
        source = cached_status() if args.offline else refresh()
        if args.command in {"refresh", "status"}:
            emit(source)
            return 0

        repository = Path(source["cache"])
        if not repository.is_dir():
            raise TokenSourceError("Локальный кэш отсутствует; сначала выполните refresh")
        records = load_records(repository, include_archive=args.include_archive)

        if args.command == "sets":
            emit({"source": source, "sets": sorted({record.token_set for record in records})})
            return 0

        if args.command == "themes":
            themes_path = repository / TOKENS_FOLDER / "$themes.json"
            themes = json.loads(themes_path.read_text(encoding="utf-8"))
            emit(
                {
                    "source": source,
                    "themes": [
                        {
                            "group": theme.get("group"),
                            "name": theme.get("name"),
                            "selectedTokenSets": theme.get("selectedTokenSets", {}),
                            "$figmaCollectionId": theme.get("$figmaCollectionId"),
                            "$figmaModeId": theme.get("$figmaModeId"),
                        }
                        for theme in themes
                    ],
                }
            )
            return 0

        matches = selected_records(
            records,
            args.query,
            exact=args.command == "get",
            token_set=args.token_set,
        )
        emit(
            {
                "source": source,
                "count": len(matches),
                "truncated": len(matches) > args.limit,
                "tokens": [record.as_dict() for record in matches[: args.limit]],
            }
        )
        return 0
    except TokenSourceError as exc:
        emit({"error": str(exc), "source": cached_status()})
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
