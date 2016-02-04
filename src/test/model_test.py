import unittest
import iris.model as wm

class ModelTest(unittest.TestCase):

   def test_model(self):
     m = wm.load()
     self.assertIsNotNone(m)



