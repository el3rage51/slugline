import unittest

from slugline import empty_slug, is_slug, slug_count, slug_length, slugify, slugify_lines, truncated, unique_slugs


class SluglineTest(unittest.TestCase):
    def test_basic(self) -> None:
        self.assertEqual(slugify("Hello, World!"), "hello-world")
        self.assertEqual(slugify("  a--b  "), "a-b")
        self.assertEqual(slugify("abcdef", 3), "abc")
        self.assertEqual(slugify_lines("Hello\n\nA B"), ["hello", "a-b"])
        self.assertTrue(is_slug("hello-world"))
        self.assertFalse(is_slug("Hello"))
        self.assertEqual(unique_slugs("Hello\nhello\nA B"), ["hello", "a-b"])
        self.assertEqual(slug_length("Hello, World!"), 11)
        self.assertTrue(truncated("Hello, World!", 5))
        self.assertFalse(truncated("hi", 60))
        self.assertTrue(empty_slug("!!!"))
        self.assertFalse(empty_slug("Hi"))
        self.assertEqual(slug_count("Hello\n\nA B"), 2)


if __name__ == "__main__":
    unittest.main()
