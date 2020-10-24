import unittest
from ..words.stopwords import remove_stopwords
from ..words.text import clear_text, clear_texts


class WordsTestCase(unittest.TestCase):

    def test_remove_stopwords(self):
        original_text = "Falar é muito fácil"
        self.assertEqual(remove_stopwords(original_text), "Falar fácil")

    def test_clear_text(self):
        original_text = "Falar é fácil. Mostre-me o código."
        self.assertEqual(clear_text(original_text), 'falar fácil mostre-me código')

    def test_clear_text_list(self):
        original_list = [
            "Falar é fácil. Mostre-me o código.",
            "É fácil escrever código. Difícil é escrever código que funcione."
        ]

        expected_list = [
            "falar fácil mostre-me código",
            "fácil escrever código difícil escrever código funcione"
        ]

        self.assertListEqual(clear_texts(original_list), expected_list)
