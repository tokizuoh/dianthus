import unittest

from vowel import vowel


class TestExtractVowel(unittest.TestCase):
    def test_extract_vowel(self):
        value = 'amana'

        expected = 'aaa'
        actual = vowel.extract(value)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()