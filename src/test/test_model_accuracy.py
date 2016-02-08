import unittest
import json
import os.path as path

import numpy as np
from sklearn.metrics import confusion_matrix, hamming_loss

import iris.model as wm

def load_samples():
    sample_filename = path.join(path.dirname(__file__), "example.json")
    return [s for s in json.load(open(sample_filename)) if 'label' in s]

class ModelAccuracyTest(unittest.TestCase):
    BASELINE_LOSS = 0.15

    def setUp(self):
        self.model = wm.load()
        self.samples = load_samples()

    def test_calc_hamming_loss(self):
        labels_true = [s['label'] for s in self.samples]
        data = [s['info'] for s in self.samples]

        labels_pred = self.model.predict(data)
        loss = hamming_loss(labels_true, labels_pred)

        self.assertLess(loss, self.BASELINE_LOSS)



