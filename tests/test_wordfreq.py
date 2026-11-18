import unittest
from wordfreq import get_most_common_words

class TestWordFreq(unittest.TestCase):
    def test_basic_counting(self):
        text = "Hello world hello world"
        expected = [("hello", 2), ("world", 2)]
        self.assertEqual(get_most_common_words(text, 2), expected)

    def test_case_insensitivity(self):
        text = "Hello hello HELLO"
        expected = [("hello", 3)]
        self.assertEqual(get_most_common_words(text, 1), expected)

    def test_punctuation_removal(self):
        text = "Hello, world! Hello... world?"
        expected = [("hello", 2), ("world", 2)]
        self.assertEqual(get_most_common_words(text, 2), expected)

    def test_top_limit(self):
        text = "a b c d e"
        result = get_most_common_words(text, 2)
        self.assertEqual(len(result), 2)

if __name__ == '__main__':
    unittest.main()
