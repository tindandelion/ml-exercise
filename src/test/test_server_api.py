import unittest
import json
import iris.server as server

def to_json(data):
    return json.dumps(data)

def response_json(response):
    return json.loads(response.data.decode("utf-8"))

class IrisApiTest(unittest.TestCase):

    def setUp(self):
        self.app = server.app
        self.client = self.app.test_client()

    def test_invalid_url(self):
        response = self.client.get('/')
        self.assertEqual(404, response.status_code)

    def test_correct_request(self):
        request_url = '/iris/v1/predict'
        body = to_json({'sample': [1, 2, 3, 4]})
        response = self.client.post(request_url, content_type="application/json", data=body)
        print(type(response))

        self.assertEqual(200, response.status_code)
        self.assertEqual({'label': 2}, response_json(response))


