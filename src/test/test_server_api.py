import unittest
import json
import iris.server as server

def to_json(data):
    return json.dumps(data)

def response_json(response):
    return json.loads(response.data.decode("utf-8"))

class IrisApiTest(unittest.TestCase):
    request_url = '/iris/v1/predict'

    def setUp(self):
        self.app = server.app
        self.client = self.app.test_client()

    def test_invalid_url(self):
        response = self.client.get('/')
        self.assertEqual(404, response.status_code)

    def test_correct_request(self):
        body = to_json({'sample': [1, 2, 3, 4]})
        response = self.client.post(self.request_url, content_type="application/json", data=body)
        self.assertValidResponse(response)

    def test_incorrect_request_invalid_content_type(self):
        response = self.client.post(self.request_url, content_type="text/plain", data="Blah")
        self.assertBadRequest(response, "Request Content-Type != application/json")

    def assertBadRequest(self, response, expected_message):
        self.assertEqual(400, response.status_code, "Response status code is BAD_REQUEST")


    def assertValidResponse(self, response):
        self.assertEqual(200, response.status_code, "Response status code is OK")
        self.assertEqual("application/json", response.content_type, "Response content type")
        self.assertTrue(len(response.data) > 0, "Response contains data")

        data = json.loads(response.data.decode("utf-8"))
        self.assertTrue('label' in data, "Response data contains label field")

        label = data['label']
        self.assertTrue(type(label) == int, "Label is integer")



