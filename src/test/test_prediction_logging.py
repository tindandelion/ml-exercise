import unittest
import json

import iris.predictor as pred

stub_predictor = (lambda sample: 42)

class LoggingPredictionTest(unittest.TestCase):
    def setUp(self):
        self.logged_message = None
    
    def test_log_prediction_results(self):
        sample = [1, 2, 3, 4]
        
        predictor = pred.with_logging(stub_predictor, logger=self)
        predictor(sample)
        
        data = json.loads(self.logged_message)
        self.assertEqual(sample, data.get('sample'), "Sample data is recorded")
        self.assertEqual(42, data.get('label'), "Label value is provided")
        self.assertTrue('performance_time' in data, "Performance data is recorded")

    def test_pass_result_label_up(self):
        predictor = pred.with_logging(stub_predictor, logger=self)      
        label = predictor([1, 2, 3, 4])
        self.assertEqual(42, label)

    def test_put_extras_to_log(self):
        extra = {'extra_data': 'Lorem Ipsum'}
        predictor = pred.with_logging(stub_predictor, logger=self, extra=extra)      

        predictor([1, 2, 3, 4])

        data = json.loads(self.logged_message)
        self.assertEquals(extra, data.get('extra'))
        
    # Logging interface
    def info(self, message):
        self.logged_message = message
        
        

