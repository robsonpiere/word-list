import unittest
from ..words.stopwords import remove_stopwords
from ..words.text import clear_text, clear_texts
from ..words.vocabulary import generate_words_list, generate_two_words_list


class WordsTestCase(unittest.TestCase):

    def test_remove_stopwords(self):
        original_text = "Falar é muito fácil"
        self.assertEqual(remove_stopwords(original_text), "Falar fácil")

    def test_clear_text(self):
        original_text = "Falar é fácil. Mostre-me o código."
        self.assertEqual(clear_text(original_text), 'falar fácil mostre código')

    def test_clear_text_list(self):
        original_list = [
            "Falar é fácil. Mostre-me o código.",
            "É fácil escrever código. Difícil é escrever código que funcione."
        ]

        expected_list = [
            "falar fácil mostre código",
            "fácil escrever código difícil escrever código funcione"
        ]

        self.assertListEqual(clear_texts(original_list), expected_list)

    def test_words_list(self):
        original_list = [
            "A minha lista de palavras é pequena.",
            "Eu acho que já fiz uma lista de palavras na faculdade ?"
        ]
        clear_list = clear_texts(original_list)
        expected_list = [
            'lista', 'palavras', 'pequena', 'acho', 'fiz', 'faculdade'
        ]
        self.assertListEqual(generate_words_list(clear_list), expected_list)

    def test_two_words_list(self):
        original_list = [
            "Falar é fácil. Mostre-me o código.",
            "É fácil escrever código. Difícil é escrever código que funcione."
        ]
        clear_list = clear_texts(original_list)
        expected_list = [
            'falar fácil', 'fácil mostre', 'mostre código', 'fácil escrever', 'escrever código', 'código difícil',
            'difícil escrever', 'código funcione'
        ]
        self.assertListEqual(generate_two_words_list(clear_list), expected_list)
