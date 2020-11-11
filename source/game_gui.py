# -*- coding: utf-8 -*-
''' Graphical User Interface for EduQuiz'''
import tkinter as tk
import game_controller as gc
import game_data as gd
import random as rd

class Gui:
    _top = tk.Tk()
    _top.resizable(0,0)
    _quiz_frame = tk.Frame(_top, bg='grey')
    _edit_frame = tk.Frame(_top, bg='blue')
    
    @classmethod
    def verify(cls):
        user_inp = cls.quiz_user_inp.get()
        cls.q.set_user_answer(user_inp)
        cls.quiz_console.insert(tk.INSERT, '\n'+str(cls.q.verify()))
    @classmethod
    def next_question(cls):
        cls.quiz_console.delete(1.0, tk.END)
        questions = gd.load_question('questions.csv', 4)
        cls.q = rd.choice(questions)
        cls.quiz_console.insert(1.0, cls.q.get_text())
        
    @classmethod   
    def write_Question(cls):
        q_type = 'QandA'
        text = cls.new_question_entry.get()
        answer = cls.new_answer_entry.get()
        gd.write_q2csv('questions.csv', q_type, text, answer)
        cls.new_question_entry.delete(0, tk.END)
        cls.new_answer_entry.delete(0, tk.END)
        
    @classmethod
    def run(cls):
        # Two Frames
        EDIT = cls._edit_frame
        QUIZ = cls._quiz_frame
        TOP = cls._top
        # Load Question
        cls.button_next_question = tk.Button(TOP, text='Next Question',
                                       command= cls.next_question, bg='grey')
        cls.button_next_question.grid(row=0, column=1)
        # Init Quiz Frame
        QUIZ.grid(row=0, column=0)
        var_quiz_label = tk.StringVar()
        cls.quiz_label = tk.Label(QUIZ, textvariable=var_quiz_label)
        var_quiz_label.set('Question')
        cls.quiz_label.pack(side=tk.TOP, fill=tk.X)
        # Consol
        cls.var_consol = tk.StringVar()
        cls.quiz_console = tk.Text(QUIZ, width=25, height=5)
        cls.quiz_console.pack(side=tk.TOP, fill=tk.X)
        # User Input
        cls.quiz_inp_label = tk.Label(QUIZ, text='Enter answer below:')
        cls.quiz_inp_label.pack(side=tk.TOP, fill=tk.X)        
        cls.quiz_user_inp = tk.Entry(QUIZ, width=25)
        cls.quiz_user_inp.pack(side=tk.TOP, fill=tk.X)
        cls.button_verify = tk.Button(QUIZ, text='Enter',command=cls.verify, bg='grey')
        cls.button_verify.pack(side=tk.TOP, fill=tk.X)
        
        # Init Editor Frame
        EDIT.grid(row=0, column=2)
        var_edit_label = tk.StringVar()
        cls.edit_label = tk.Label(EDIT, textvariable=var_edit_label)
        var_edit_label.set('Editor')
        cls.edit_label.pack(side=tk.TOP, fill=tk.X)
        # new question
        cls.new_question_label = tk.Label(EDIT, text='Enter question text below:')
        cls.new_question_label.pack(side=tk.TOP, fill=tk.X)
        cls.new_question_entry = tk.Entry(EDIT, font=5, width= 25)
        cls.new_question_entry.pack(side=tk.TOP,fill=tk.X)
        
        cls.new_answer_label = tk.Label(EDIT, text='Enter correct answer text below:')
        cls.new_answer_label.pack(side=tk.TOP, fill=tk.X)
        cls.new_answer_entry = tk.Entry(EDIT, font=5, width= 25)
        cls.new_answer_entry.pack(side=tk.TOP,fill=tk.X)

        # cls.new_wrong1_label = tk.Label(EDIT, text='Enter first wrong answer text below:')
        # cls.new_wrong1_label.pack(side=tk.TOP, fill=tk.X)
        # cls.new_wrong1_entry = tk.Entry(EDIT, font=5, width= 25)
        # cls.new_wrong1_entry.pack(side=tk.TOP,fill=tk.X)

        # cls.new_wrong2_label = tk.Label(EDIT, text='Enter second wrong answer text below:')
        # cls.new_wrong2_label.pack(side=tk.TOP, fill=tk.X)
        # cls.new_wrong2_entry = tk.Entry(EDIT, font=5, width= 25)
        # cls.new_wrong2_entry.pack(side=tk.TOP,fill=tk.X)
        
        cls.button_submit_question = tk.Button(EDIT, text='Save Question',
                                               command= cls.write_Question, bg='grey')
        cls.button_submit_question.pack(side=tk.BOTTOM, fill=tk.X)
        cls._top.mainloop()

Gui.run()