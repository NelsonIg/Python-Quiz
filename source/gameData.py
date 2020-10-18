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
    '''
    def __init__(self, text: str, answer: str):
        # check parameter
        if not isinstance(text, str):
            raise TypeError('text must be string!')  
        if not isinstance(answer, str):
            raise TypeError('answer must be string!')
        self._text = text
        self._answer = answer
    
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

class estimQuestion(Question):
    def __init__(self, text: str, answer: str):
        # check parameter
        if not isinstance(text, str):
            raise TypeError('text must be string!')  
        if not isinstance(answer, str):
            raise TypeError('answer must be string!')
        super().__init__(text, answer)
        self._userInp = None
    
    def setUserInp(self, userInp: str):
        # check input
        if not isinstance(userInp, str):
            raise TypeError('userInp must be string!')
        self._userInp = userInp
        
    def getUserInp(self):
        return self._userInp
    
    def verify(self):
        '''
        Returns -1: no user input, True, False
        '''
        if self._userInp:
            return self._userInp == self._answer
        return -1
        
e = estimQuestion('estimation', 'B')
e.setUserInp('B')
print(e.verify())

if __name__ == '__main__':
    import doctest
    doctest.testmod()