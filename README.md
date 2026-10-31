# slugline

Make a lowercase hyphenated slug from a title. Punctuation becomes a single hyphen. The result is trimmed to `maxlen`.

```python
from slugline import slugify, slugify_lines, is_slug, unique_slugs, slug_length, truncated, empty_slug, slug_count, longest_slug, shortest_slug, slug_gap, same_length, slug_over, slug_even

slugify("Hello, World!")  # "hello-world"
slugify_lines("Hello\nA B")  # ["hello", "a-b"]
is_slug("hello-world")  # True
unique_slugs("Hello\nhello")  # ["hello"]
```

```bash
python -m unittest test_slugline.py
```

MIT
