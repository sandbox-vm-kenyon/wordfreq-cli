import unittest
import os
import subprocess
from wordfreq import get_most_common_words

class TestWordFreqLogic(unittest.TestCase):
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

class TestWordFreqCLI(unittest.TestCase):
    def setUp(self):
        self.test_file = "test_input.txt"

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def run_cli(self, args):
        cmd = ["python3", "wordfreq.py"] + args
        result = subprocess.run(cmd, capture_output=True, text=True)
        return result.stdout

    def test_cli_reads_file(self):
        with open(self.test_file, "w") as f:
            f.write("apple banana apple")
        output = self.run_cli([self.test_file, "--top", "2"])
        self.assertIn("apple: 2", output)
        self.assertIn("banana: 1", output)

    def test_cli_default_top_10(self):
        # Create a file with 15 unique words
        with open(self.test_file, "w") as f:
            f.write(" ".join([str(i) for i in range(15)]))
        output = self.run_cli([self.test_file])
        lines = [line for line in output.splitlines() if line.strip()]
        self.assertEqual(len(lines), 10)

    def test_cli_custom_top(self):
        with open(self.test_file, "w") as f:
            f.write("a a b b c c d d e e")
        output = self.run_cli([self.test_file, "--top", "3"])
        lines = [line for line in output.splitlines() if line.strip()]
        self.assertEqual(len(lines), 3)

if __name__ == '__main__':
    unittest.main()
