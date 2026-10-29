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


def slug_length(text: str, maxlen: int = 60) -> int:
    return len(slugify(text, maxlen))


def truncated(text: str, maxlen: int = 60) -> bool:
    if maxlen < 1:
        raise ValueError("长度至少为 1")
    raw = _NON.sub("-", (text or "").strip().lower()).strip("-")
    return len(raw) > maxlen


def empty_slug(text: str, maxlen: int = 60) -> bool:
    return slugify(text, maxlen) == ""


def slug_count(text: str, maxlen: int = 60) -> int:
    return len([item for item in slugify_lines(text, maxlen) if item])


def longest_slug(text: str, maxlen: int = 60) -> int:
    items = [item for item in slugify_lines(text, maxlen) if item]
    if not items:
        return 0
    return max(len(item) for item in items)


def shortest_slug(text: str, maxlen: int = 60) -> int:
    items = [item for item in slugify_lines(text, maxlen) if item]
    if not items:
        return 0
    return min(len(item) for item in items)


def slug_gap(text: str, maxlen: int = 60) -> int:
    return longest_slug(text, maxlen) - shortest_slug(text, maxlen)


def same_length(text: str, maxlen: int = 60) -> bool:
    return slug_count(text, maxlen) > 0 and slug_gap(text, maxlen) == 0

def slug_over(text: str, limit: int, maxlen: int = 60) -> bool:
    if limit < 0:
        raise ValueError("上限不能为负")
    return longest_slug(text, maxlen) > limit
