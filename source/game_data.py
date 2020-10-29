# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 14:36:36 2020

@author: nelso
"""
import os
import pandas as pd

class Question:
    '''
    Base Class for Questions
        ATTR: __text, __answer, _user_answer & _type= 'QandA'
        METHS: setter & getter
    DocTest
    >>> q = Question('text', 'answer')
    >>> q.get_type()
    'QandA'
    >>> q.set_text('new text')
    >>> q.get_text()
    'new text'
    >>> q.set_answer('new answer')
    >>> q.get_answer()
    'new answer'
    >>> q.verify()
    -1
    >>> q.set_user_answer('99')
    >>> q.get_user_answer()
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
        self._user_answer = None
        self._type = "QandA"
    
    # Setter & Getter ---------------------------------------------------------
    def set_text(self, text: str):
        # check user input
        if not isinstance(text, str):
            raise TypeError('text must be string!')
        self._text = text
    
    def get_text(self):
        return self._text
   
    def set_answer(self, answer: str):
        # check user input
        if not isinstance(answer, str):
            raise TypeError('answer must be string!')
        self._answer = answer
    
    def get_answer(self):
        return self._answer

    def set_user_answer(self, user_answer: str):
        # check input
        if not isinstance(user_answer, str):
            raise TypeError('user_answer must be string!')
        self._user_answer = user_answer
        
    def get_user_answer(self):
        return self._user_answer
    
    def get_type(self):
        return self._type
    # -------------------------------------------------------------------------
    
    def verify(self):
        '''
        Return -1: no user input, True, False
        '''
        if self._user_answer:
            return self._user_answer == self._answer
        return -1

class MCQ(Question):
    '''
    Multiple Choice Question
    
    DocTest
    >>> m = MCQ('test', 'right answer')
    >>> m.get_type()
    'MCQ'
    >>> m.set_wrong('wrong1', 'wrong2')
    >>> m.get_wrong()
    ('wrong1', 'wrong2')
    >>> m.set_user_answer(m.get_wrong()[0])
    >>> m.verify()
    False
    '''
    
    def __init__(self, text, answer, wrong_one=None,  wrong_two=None):
        # check parameter
        if not isinstance(text, str):
            raise TypeError('text must be string!')  
        if not isinstance(answer, str):
            raise TypeError('answer must be string!')
        super().__init__(text, answer)
        self._wrong_one = wrong_one
        self._wrong_two = wrong_two
        self._user_choice = None
        self._type = 'MCQ'
    
    def set_wrong(self, wrong_one: str, wrong_two: str):
        # check parameters
        if not isinstance(wrong_one, str) or not isinstance(wrong_two, str):
            raise TypeError('set_wrong recuires string as arguments')
        self._wrong_one, self._wrong_two = wrong_one, wrong_two
    
    def get_wrong(self):
        return self._wrong_one, self._wrong_two
    
def writeQtoCsv(filename: str, q_type: str, text: str,
                answer: str, wrong1='', wrong2=''):
    ''' writes question to filname.csv'''
    if os.path.exists('./'+filename):
        # file already in repository
        with open(filename, 'r') as f:
            first_line = f.readline()
        if first_line=='type,text,answer,wrong1,wrong2\n':
            # file already initialized
            with open(filename, 'a') as f:
                f.write(q_type+','+text+','+answer+','+wrong1+','+wrong2+'\n')
        else:
            with open(filename, 'w') as f:
                f.write('type,text,answer,wrong1,wrong2\n')
                f.write(q_type+','+text+','+answer+','+wrong1+','+wrong2+'\n')
    else:
        with open(filename, 'w') as f:
            f.write('type,text,answer,wrong1,wrong2\n')
            f.write(q_type+','+text+','+answer+','+wrong1+','+wrong2+'\n')

def load_question(filename: str, quest_no: int):
    ''' load question from filname.csv'''
    if not os.path.exists('./'+filename):
        raise Exception('file not found')
    df = pd.read_csv(filename, nrows=quest_no)
    questions = list()
    for idx, row in df.iterrows():
        if row['type']=='QandA':
            questions.append(Question(row['text'], row['answer']))
        elif row['type']=='MCQ':
            questions.append(MCQ(row['text'], row['answer'],
                                 row['wrong1'], row['wrong2']))
        else:
            pass
    return questions

    
if __name__ == '__main__':
    import doctest
    doctest.testmod()