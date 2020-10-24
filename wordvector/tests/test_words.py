import unittest
from ..words.stopwords import remove_stopwords


class WordsTestCase(unittest.TestCase):

    def test_remove_stopwords(self):
        original_text = "Falar é muito fácil"
        self.assertEqual(remove_stopwords(original_text), "Falar fácil")


if __name__ == '__main__':
    unittest.main()
