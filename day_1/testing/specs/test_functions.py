import unittest
from functions import my_functions

class TestMyFunctions(unittest.TestCase):

  def test_greet(self):
    greeting_result = my_functions.greet("Zsolt", "morning")
    self.assertEqual(greeting_result, "Good morning, Zsolt.")

