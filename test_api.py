import unittest
import json
from api import app

class TestAPI(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_converter_numero_inteiro(self):
        response = self.app.post('/converter',
                               data=json.dumps({'numero': 42}),
                               content_type='application/json')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['extenso'], 'quarenta e dois')

    def test_converter_numero_decimal(self):
        response = self.app.post('/converter',
                               data=json.dumps({'numero': 1.5}),
                               content_type='application/json')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['extenso'], 'um vírgula cinco')

    def test_converter_numero_negativo(self):
        response = self.app.post('/converter',
                               data=json.dumps({'numero': -15}),
                               content_type='application/json')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['extenso'], 'menos quinze')

    def test_erro_sem_numero(self):
        response = self.app.post('/converter',
                               data=json.dumps({}),
                               content_type='application/json')
        self.assertEqual(response.status_code, 400)

    def test_erro_numero_invalido(self):
        response = self.app.post('/converter',
                               data=json.dumps({'numero': 'abc'}),
                               content_type='application/json')
        self.assertEqual(response.status_code, 400)

if __name__ == '__main__':
    unittest.main() 