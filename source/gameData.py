# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 14:36:36 2020

@author: nelso
"""


class Question:
    '''
    Base Class for Questions
        ATTR: __text & __answer
        METHS: setter & getter
    DocTest
    >>> q = Question('text', 'answer')
    >>> q.setText('new text')
    >>> q.getText()
    'new text'
    >>> q.setAnswer('new answer')
    >>> q.getAnswer()
    'new answer'
    >>> q.verify()
    -1
    >>> q.setUserAnswer('99')
    >>> q.getUserAnswer()
    '99'
    >>> q.verify()
    False
    '''
    
    def __init__(self, text: str, answer: str):
        # check parameter
        if not isinstance(text, str):
            raise TypeError('text must be string!')  
        if not isinstance(answer, str):
            raise TypeError('answer must be string!')
        self._text = text
        self._answer = answer
        self._userAnswer = None
    
    def setText(self, text: str):
        # check user input
        if not isinstance(text, str):
            raise TypeError('text must be string!')
        self._text = text
    
    def getText(self):
        return self._text
   
    def setAnswer(self, answer: str):
        # check user input
        if not isinstance(answer, str):
            raise TypeError('answer must be string!')
        self._answer = answer
    
    def getAnswer(self):
        return self._answer

    def setUserAnswer(self, userAnswer: str):
        # check input
        if not isinstance(userAnswer, str):
            raise TypeError('userAnswer must be string!')
        self._userAnswer = userAnswer
        
    def getUserAnswer(self):
        return self._userAnswer
    
    def verify(self):
     '''
     Return -1: no user input, True, False
     '''
     if self._userAnswer:
         return self._userAnswer == self._answer
     return -1
    
       
class MCQ(Question):
    '''
    Multiple Choice Question
    
    DocTest
    >>> m = MCQ('test', 'right answer')
    >>> m.setWrong('wrong1', 'wrong2')
    >>> m.getWrong()
    ('wrong1', 'wrong2')
    >>> m.setUserAnswer(m.getWrong()[0])
    >>> m.verify()
    False
    '''
    
    def __init__(self, text, answer):
        # check parameter
        if not isinstance(text, str):
            raise TypeError('text must be string!')  
        if not isinstance(answer, str):
            raise TypeError('answer must be string!')
        super().__init__(text, answer)
        self._wrongOne = None
        self._wrongTwo = None
        self._userChoice = None
    
    def setWrong(self, wrongOne: str, wrongTwo: str):
        # check parameters
        if not isinstance(wrongOne, str) or not isinstance(wrongTwo, str):
            raise TypeError('setWrong recuires string as arguments')
        self._wrongOne, self._wrongTwo = wrongOne, wrongTwo
    
    def getWrong(self):
        return self._wrongOne, self._wrongTwo
    

    
if __name__ == '__main__':
    import doctest
    doctest.testmod()