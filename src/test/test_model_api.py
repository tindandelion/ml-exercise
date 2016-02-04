import unittest
import iris.model as wm

class ModelApiTest(unittest.TestCase):

    def setUp(self):
        self.model = wm.load()

    def test_load_model(self):
        self.assertIsNotNone(self.model)

    def test_incorrect_model_parameters(self):
        self.assertIsNone(self.model.predict(None), "None as a sample")
        self.assertIsNone(self.model.predict([]), "Empty list as a sample")
        self.assertIsNone(self.model.predict([[1, 2]]), "Too few data in the sample")
        self.assertIsNone(self.model.predict([[1, 2, 3, 4, 5]]), "Too much data in the sample")
        self.assertIsNone(self.model.predict([[1, 2, 3, "blah"]]), "Incorrect data type")

    def test_correct_data(self):
        labels = self.model.predict([[6.0, 2.9, 4.5, 1.5]])
        self.assertEqual(1, labels[0])
