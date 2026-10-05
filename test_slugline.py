import unittest

from slugline import is_slug, slugify, slugify_lines, unique_slugs


class SluglineTest(unittest.TestCase):
    def test_basic(self) -> None:
        self.assertEqual(slugify("Hello, World!"), "hello-world")
        self.assertEqual(slugify("  a--b  "), "a-b")
        self.assertEqual(slugify("abcdef", 3), "abc")
        self.assertEqual(slugify_lines("Hello\n\nA B"), ["hello", "a-b"])
        self.assertTrue(is_slug("hello-world"))
        self.assertFalse(is_slug("Hello"))
        self.assertEqual(unique_slugs("Hello\nhello\nA B"), ["hello", "a-b"])


if __name__ == "__main__":
    unittest.main()
