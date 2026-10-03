import unittest

from slugline import is_slug, slugify, slugify_lines


class SluglineTest(unittest.TestCase):
    def test_basic(self) -> None:
        self.assertEqual(slugify("Hello, World!"), "hello-world")
        self.assertEqual(slugify("  a--b  "), "a-b")
        self.assertEqual(slugify("abcdef", 3), "abc")
        self.assertEqual(slugify_lines("Hello\n\nA B"), ["hello", "a-b"])
        self.assertTrue(is_slug("hello-world"))
        self.assertFalse(is_slug("Hello"))


if __name__ == "__main__":
    unittest.main()
