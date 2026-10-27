import unittest

from slugline import empty_slug, is_slug, longest_slug, same_length, shortest_slug, slug_count, slug_gap, slug_length, slugify, slugify_lines, truncated, unique_slugs


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
        self.assertEqual(longest_slug("Hello\n\nA B"), 5)
        self.assertEqual(longest_slug("!!!"), 0)
        self.assertEqual(shortest_slug("Hello\n\nA B"), 3)
        self.assertEqual(shortest_slug("!!!"), 0)
        self.assertEqual(slug_gap("Hello\n\nA B"), 2)
        self.assertEqual(slug_gap("!!!"), 0)
        self.assertFalse(same_length("Hello\n\nA B"))
        self.assertTrue(same_length("Hello\nWorld"))


if __name__ == "__main__":
    unittest.main()
