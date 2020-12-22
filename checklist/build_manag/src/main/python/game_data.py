# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 14:36:36 2020

@author: nelso
"""
import os
import pandas as pd

def is_string(var, var_name: str):
    ''' Check if var is instance of STRING
        Does nothing if var is string, raises TypeError if not
    '''
    if not isinstance(var, str):
            raise TypeError(var_name+' must be string!')
class Question:
    
    def __init__(self, text: str, answer: str):
        # check parameter
        is_string(text, 'text')
        is_string(answer, 'answer')
        self._text = text
        self._answer = answer
        self._user_answer = None
        self._type = "QandA"
    
    # Setter & Getter ---------------------------------------------------------
    def set_text(self, text: str):
        # check user input
        is_string(text, 'text')
        self._text = text
    
    def get_text(self):
        return self._text
   
    def set_answer(self, answer: str):
        # check user input
        is_string(answer, 'answer')
        self._answer = answer
    
    def get_answer(self):
        return self._answer

    def set_user_answer(self, user_answer: str):
        # check input
        is_string(user_answer, 'user_answer')
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
     
    def __init__(self, text, answer, wrong_one=None,  wrong_two=None):
        # check parameter
        is_string(text, 'text')
        is_string(answer, 'answer')
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
    
def write_q2csv(filename: str, q_type: str, text: str,
                answer: str, wrong1='', wrong2=''):
    ''' writes question to filname.csv'''
    COLUMNS = 'type,text,answer,wrong1,wrong2'
    if os.path.exists('./'+filename):
        # file already in repository
        with open(filename, 'r') as f:
            first_line = f.readline()
        if first_line==COLUMNS+'\n':
            # file already initialized
            with open(filename, 'a') as f:
                f.write(q_type+','+text+','+answer+','+wrong1+','+wrong2+'\n')
        else:
            with open(filename, 'w') as f:
                f.write(COLUMNS+'\n')
                f.write(q_type+','+text+','+answer+','+wrong1+','+wrong2+'\n')
    else:
        with open(filename, 'w') as f:
            f.write(COLUMNS+'\n')
            f.write(q_type+','+text+','+answer+','+wrong1+','+wrong2+'\n')

def load_question(filename: str, quest_no: int):
    ''' load question from filname.csv'''
    if not os.path.exists('./'+filename):
        raise FileNotFoundError (filename+' not found')
    df = pd.read_csv(filename, nrows=quest_no)
    questions = list()
    for idx, row in df.iterrows():
        if row['type']=='QandA':
            questions.append(Question(row['text'], row['answer']))
        elif row['type']=='MCQ':
            questions.append(MCQ(row['text'], row['answer'],
                                 row['wrong1'], row['wrong2']))
        else:
            # Question Type not unknown
            pass
    return questions


