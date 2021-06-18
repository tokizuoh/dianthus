import unittest

from vowel import vowel


class TestExtractVowel(unittest.TestCase):
    def test_extract_vowel_normal(self):
        value = 'amana'

        expected = 'aaa'
        actual = vowel.extract(value)
        self.assertEqual(expected, actual)

    def test_extract_vowel_include_chi(self):
        value = 'chiyuki'

        expected = 'iui'
        actual = vowel.extract(value)
        self.assertEqual(expected, actual)

    def test_extract_vowel_continuous_vowel(self):
        value = 'oosaki'

        expected = 'ooai'
        actual = vowel.extract(value)
        self.assertEqual(expected, actual)

    def test_extract_vowel_continuous_vowel(self):
        value = 'oosaki'

        expected = 'ooai'
        actual = vowel.extract(value)
        self.assertEqual(expected, actual)
    
    def test_extract_vowel_include_jyo(self):
        value = 'saijyo'

        expected = 'aio'
        actual = vowel.extract(value)
        self.assertEqual(expected, actual)

    def test_extract_vowel_only_vowel(self):
        value = 'aaa'

        expected = 'aaa'
        actual = vowel.extract(value)
        self.assertEqual(expected, actual)

    def test_extract_vowel_include_na(self):
        value = 'natsuha'

        expected = 'aua'
        actual = vowel.extract(value)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()