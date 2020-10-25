import unittest
from ..words.vocabulary import generate_vocabulary


class VocabularyTestCase(unittest.TestCase):

    def test_vocabulary(self):
        original_list = [
            "Falar é fácil. Mostre-me o código.",
            "É fácil escrever código. Difícil é escrever código que funcione."
        ]
        vocabulary = generate_vocabulary(texts=original_list)
        expected = {
            'textos': ['falar fácil mostre código', 'fácil escrever código difícil escrever código funcione'],
            'listaDePalavras': ['falar', 'fácil', 'mostre', 'código', 'escrever', 'difícil', 'funcione'],
            'listaDeDuasPalavras': [
                'falar fácil', 'fácil mostre', 'mostre código', 'fácil escrever', 'escrever código',
                               'código difícil', 'difícil escrever', 'código funcione'
            ],
            'vetorDePalavras': [[1, 1, 1, 1, 0, 0, 0], [0, 1, 0, 2, 2, 1, 1]],
            'vetorDeDuasPalavras': [[1, 1, 1, 0, 0, 0, 0, 0], [0, 0, 0, 1, 2, 1, 1, 1]]
        }
        self.assertDictEqual(vocabulary, expected)

    def test_vocabulary_with_filter(self):
        original_list = [
            "Falar é fácil. Mostre-me o código.",
            "É fácil escrever código. Difícil é escrever código que funcione."
        ]
        vocabulary = generate_vocabulary(texts=original_list, result_filter =['textos', 'listaDeDuasPalavras', 'vetorDeDuasPalavras'])
        expected = {
            'textos': ['falar fácil mostre código', 'fácil escrever código difícil escrever código funcione'],
            'listaDeDuasPalavras': [
                'falar fácil', 'fácil mostre', 'mostre código', 'fácil escrever', 'escrever código',
                'código difícil', 'difícil escrever', 'código funcione'
            ],
            'vetorDeDuasPalavras': [[1, 1, 1, 0, 0, 0, 0, 0], [0, 0, 0, 1, 2, 1, 1, 1]]
        }

        self.assertDictEqual(vocabulary, expected)


