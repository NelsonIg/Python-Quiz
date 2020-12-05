import unittest
import builtins
from unittest.mock import Mock
import mock
import game_controller as gc

class ControllerTest(unittest.TestCase):
    def test_start_quiz(self):
        # Mock Question
        q = Mock()
        q.text = '1+1'
        q.answer = '2'
        q.get_text.return_value = '1+1'
        q.get_answer.return_value = '2'
        with mock.patch.object(builtins, 'input', lambda _: '2'):
            with mock.patch.object(builtins, 'isinstance', lambda x, y: True):
            quiz = gc.Quiz(q)
        
        
