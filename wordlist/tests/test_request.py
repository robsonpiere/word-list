import unittest
from json import dumps, loads
from wordlist.app import create_app
from flask import Response


class CompleteRequestTestCase(unittest.TestCase):
    body_example = {
        "textos": [
            "Atirei o pau no gato",
            "Mas o gato não morreu",
            "Dona Chica admirou-se",
            "Do berro, do berro que o gato deu Miau!"
        ]
    }

    def setUp(self) -> None:
        self.app = create_app()
        self.client = self.app.test_client()

    def request(self, data: dict) -> Response:
        data = dumps(data)
        return self.client.post('/vocabulary', data=data, content_type='application/json')

    def test_request_complete(self):
        response = self.request(self.body_example)
        response_body = loads(response.data)
        self.assertEqual(200, response.status_code)
        self.assertEqual('application/json', response.content_type)
        self.assertIn('textos', response_body)
        self.assertListEqual(
            ['atirei pau', 'pau gato', 'gato morreu', 'dona chica', 'chica admirou', 'berro berro', 'berro gato',
             'gato deu', 'deu miau'],
            response_body.get('listaDeDuasPalavras')
        )

    def test_request_with_filter(self):
        body = self.body_example
        body['filtrar'] = ['listaDeDuasPalavras', 'vetorDeDuasPalavras', 'listaDePalavras']
        response = self.request(body)
        response_body = loads(response.data)
        self.assertEqual(200, response.status_code)
        self.assertEqual('application/json', response.content_type)
        self.assertNotIn('textos', response_body)
        self.assertNotIn('vetorDePalavras', response_body)
        self.assertIn('listaDeDuasPalavras', response_body)
        self.assertIn('vetorDeDuasPalavras', response_body)
        self.assertIn('listaDePalavras', response_body)
