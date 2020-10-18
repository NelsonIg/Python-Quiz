# -*- coding: utf-8 -*-
import gameData as gd

class Quiz:
    def __init__(self, *questions):
        for question in questions:
            #check if questions are all instances  of class Question
            if not isinstance(question, gd.Question):
                raise TypeError(
                    'All questions  must be instance of class Question')
        self._questions = questions
        self._score = 0
    def setScore(self, score: int):
        if not isinstance(score, int):
            raise TypeError('score must be int')
        self._score = score
    def getScore(self)-> int:
        return self._score
    
    def displayQuestion(self, question):
        print(question.getText())
        
    def waitForUser(self):
        return input('[You]: ')
    
    def checkAnswer(self, question):
        return self.waitForUser() == question.getAnswer()
    
    def startQuiz(self):
        '''display one question at a time and check if user is right'''
        print('Quiz started:', f'{len(self._questions)} Questions')
        for question in self._questions:
            quiz.displayQuestion(question)
            if quiz.checkAnswer(question):
                # increas score by 1
                self.setScore(self.getScore()+1)
                print('Correct!')
            else:
                print('Not Correct!')
        print(f'You have {self.getScore()} of {len(self._questions)} right!')

questions = [gd.Question(f'text{i}', f'answer{i}') for i in range(3)]
quiz = Quiz(*questions)
quiz.startQuiz()