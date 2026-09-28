"""Turn a title into a URL slug."""
from __future__ import annotations

import re

_NON = re.compile(r"[^a-z0-9]+")


def slugify(text: str, maxlen: int = 60) -> str:
    if maxlen < 1:
        raise ValueError("长度至少为 1")
    raw = _NON.sub("-", (text or "").strip().lower()).strip("-")
    return raw[:maxlen].strip("-")
