# -*- coding: utf-8 -*-
import game_data as gd

class Quiz:
    def __init__(self, *questions):
        for question in questions:
            #check if questions are all instances  of class Question
            if not isinstance(question, gd.Question):
                raise TypeError(
                    'All questions  must be instance of class Question')
        self._questions = questions
        self._score = 0
    def set_score(self, score: int):
        if not isinstance(score, int):
            raise TypeError('score must be int')
        self._score = score
    def get_score(self)-> int:
        return self._score
    
    @staticmethod
    def display_question(question):
        print(question.get_text())
        
    @staticmethod    
    def read_user_inp():
        return input('[You]: ')
    
    def check_answer(self, question):
        return self.read_user_inp() == question.get_answer()
    
    def start_quiz(self):
        '''display one question at a time and check if user is right'''
        print('Quiz started:', f'{len(self._questions)} Questions')
        for question in self._questions:
            self.display_question(question)
            if self.check_answer(question):
                # increase score by 1
                self.set_score(self.get_score()+1)
                print('Correct!')
            else:
                print('Not Correct!')
        print(f'You have {self.get_score()} of {len(self._questions)} right!')

# questions = [gd.Question(f'text{i}', f'answer{i}') for i in range(3)]
# quiz = Quiz(*questions)
# quiz.start_quiz()