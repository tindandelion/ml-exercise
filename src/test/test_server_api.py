import unittest
import json
import iris.server as server

def to_json(data):
    return json.dumps(data)

def response_json(response):
    return json.loads(response.data.decode("utf-8"))

class IrisInputValidationTest(unittest.TestCase):
    request_url = '/iris/v1/predict'

    def setUp(self):
        self.app = server.app
        self.client = self.app.test_client()

    def test_correct_request_returns_success_response(self):
        body = to_json({'sample': [1, 2, 3, 4]})
        response = self.client.post(self.request_url, content_type="application/json", data=body)
        self.assertValidResponse(response)

    def test_incorrect_request_invalid_content_type(self):
        response = self.client.post(self.request_url, content_type="text/plain", data="Blah")
        self.assertBadRequest(response, server.INVALID_CONTENT_TYPE)

    def test_incorrect_request_no_sample(self):
        response = self.client.post(self.request_url, content_type="application/json", data=to_json({}))
        self.assertBadRequest(response, server.MISSING_SAMPLE)

    def test_incorrect_request_sample_wrong_type(self):
        data = to_json({'sample': 'rubbish'})
        response = self.client.post(self.request_url, content_type="application/json", data=data)
        self.assertBadRequest(response, server.BAD_SAMPLE)

    def test_incorrect_request_sample_wrong_type(self):
        data = to_json({'sample': 'rubbish'})
        response = self.client.post(self.request_url, content_type="application/json", data=data)
        self.assertBadRequest(response, server.BAD_SAMPLE)

    def test_incorrect_request_sample_wrong_sample_size(self):
        data = to_json({'sample': [0, 0, 0]})
        response = self.client.post(self.request_url, content_type="application/json", data=data)
        self.assertBadRequest(response, server.BAD_SAMPLE)

        data = to_json({'sample': [0, 0, 0, 0, 0]})
        response = self.client.post(self.request_url, content_type="application/json", data=data)
        self.assertBadRequest(response, server.BAD_SAMPLE)

    def test_incorrect_request_sample_wrong_sample_entry(self):
        data = to_json({'sample': [0, 0, 0, 'rubbish']})
        response = self.client.post(self.request_url, content_type="application/json", data=data)
        self.assertBadRequest(response, server.BAD_SAMPLE)

    def assertBadRequest(self, response, expected_message):
        self.assertEqual(400, response.status_code, "Response status code is BAD_REQUEST")
        self.assertEqual("application/json", response.content_type, "Response content type")

        data = json.loads(response.data.decode("utf-8"))
        self.assertTrue('message' in data, "Error response  contains 'message' field")

        message = data['message']
        self.assertEqual(expected_message, message, "Expected error message")

    def assertValidResponse(self, response):
        self.assertEqual(200, response.status_code, "Response status code is OK")
        self.assertEqual("application/json", response.content_type, "Response content type")
        self.assertTrue(len(response.data) > 0, "Response contains data")

        data = json.loads(response.data.decode("utf-8"))
        self.assertTrue('label' in data, "Response data contains label field")

        label = data['label']
        self.assertTrue(type(label) == int, "Label is integer")

class IrisModelErrorTest(unittest.TestCase):
    request_url = '/iris/v1/predict'

    def setUp(self):
        self.app = server.app
        self.client = self.app.test_client()
        
        self.orig_model = self.app.model
        self.app.model = self

    def tearDown(self):
        self.app.model = self.orig_model

    def predict(self, data): return None

    def test_when_model_returns_none_server_responds_with_error(self):
        body = to_json({'sample': [1, 2, 3, 4]})
        response = self.client.post(self.request_url, content_type="application/json", data=body)
        self.assertEqual(500, response.status_code)



