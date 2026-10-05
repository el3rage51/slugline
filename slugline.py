"""Turn a title into a URL slug."""
from __future__ import annotations

import re

_NON = re.compile(r"[^a-z0-9]+")


def slugify(text: str, maxlen: int = 60) -> str:
    if maxlen < 1:
        raise ValueError("长度至少为 1")
    raw = _NON.sub("-", (text or "").strip().lower()).strip("-")
    return raw[:maxlen].strip("-")


def is_slug(text: str, maxlen: int = 60) -> bool:
    return bool(text) and slugify(text, maxlen) == text


def slugify_lines(text: str, maxlen: int = 60) -> list[str]:
    return [slugify(line, maxlen) for line in (text or "").splitlines() if line.strip()]


def unique_slugs(text: str, maxlen: int = 60) -> list[str]:
    seen: list[str] = []
    for item in slugify_lines(text, maxlen):
        if item and item not in seen:
            seen.append(item)
    return seen
