import unittest
import json
import os.path as path

import iris.model as wm

def load_samples():
    sample_filename = path.join(path.dirname(__file__), "example.json")
    return [s for s in json.load(open(sample_filename)) if 'label' in s]

class ModelAccuracyTest(unittest.TestCase):
    BASELINE_COST = 0.42

    def setUp(self):
        self.model = wm.load()
        self.samples = load_samples()

    def test_calculate_performance_cost(self):
        table = [[0, 0, 0],
                 [0, 0, 0],
                 [0, 0, 0]]
        totals = [0, 0, 0]

        for smpl in self.samples:
            label, data = smpl['label'], smpl['info']
            pred = self.model.predict([data])[0]
            table[pred][label] += 1
            totals[label] += 1

        costs = [v/totals[j] for (i, row) in enumerate(table)
                 for (j, v) in enumerate(row) if i != j]

        self.assertLess(sum(costs), self.BASELINE_COST)
        




