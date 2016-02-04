import unittest
import json
import os.path as path

import iris.model as wm

def load_samples():
    sample_filename = path.join(path.dirname(__file__), "example.json")
    return [s for s in json.load(open(sample_filename)) if 'label' in s]


class ModelAccuracyTest(unittest.TestCase):
    MISMATCH_THRESHOLD = 0.86

    def setUp(self):
        self.model = wm.load()
        self.samples = load_samples()

    def test_prediction_accuracy(self):
        misses = [sample for sample in self.samples if self.detect_mismatch(sample)]
        mismatch_ratio = len(misses) / len(self.samples)
        self.assertLess(mismatch_ratio, self.MISMATCH_THRESHOLD)
        

    def detect_mismatch(self, sample):
        label, data = sample['label'], sample['info']
        predicted = self.model.predict([data])
        return predicted[0] == label



