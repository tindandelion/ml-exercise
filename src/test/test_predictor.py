import unittest
import iris.predictor as predictor

class PredictorTest(unittest.TestCase):

    def setUp(self):
        self.samples_to_predict = []
        self.labels_returned = [0]
        
        self.predictor = predictor.make(self)

    def test_create(self):
        pred = predictor.make(self)

    def test_pass_sample_to_model(self):
        self.predictor([1, 2, 3, 4])
        self.assertEqual([[1, 2, 3, 4]], self.samples_to_predict)

    def test_extract_label_from_model_prediction(self):
        self.labels_returned = [1]
        label = self.predictor([2, 3, 4, 5])
        self.assertEqual(1, label)

    def test_when_model_returns_none_return_none(self):
        self.labels_returned = None
        label = self.predictor([2, 3, 4, 5])
        self.assertIsNone(label)

    def test_convert_label_to_int(self):
        self.labels_returned = ["1"]
        label = self.predictor([2, 3, 4, 5])
        self.assertEqual(1, label)
        

    # Model interface
    def predict(self, samples):
        self.samples_to_predict = samples
        return self.labels_returned
    
        

    
