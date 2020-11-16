import unittest
from game_data import is_string, Question

class QuestionTest(unittest.TestCase):
   def test_is_string(self):
      self.assertIsNone(is_string('string', 'var_name'))
   def test_class_question(self):
      # test constructor
      with self.assertRaises(TypeError):
         q = Question(2,'answer')
