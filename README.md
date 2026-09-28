# slugline

Make a lowercase hyphenated slug from a title. Punctuation becomes a single hyphen. The result is trimmed to `maxlen`.

```python
from slugline import slugify

slugify("Hello, World!")  # "hello-world"
```

```bash
python -m unittest test_slugline.py
```

MIT
