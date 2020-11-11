# -*- coding: utf-8 -*-
''' Graphical User Interface for EduQuiz'''
import tkinter as tk

class Gui:
    _top = tk.Tk()
    _top.resizable(0,0)
    _quiz_frame = tk.Frame(_top, bg='grey')
    _edit_frame = tk.Frame(_top, bg='blue')
    @classmethod
    def run(cls):
        # Two Frames
        EDIT = cls._edit_frame
        QUIZ = cls._quiz_frame
        
        # Init Quiz Frame
        QUIZ.pack(side=tk.LEFT)
        var_quiz_label = tk.StringVar()
        quiz_label = tk.Label(QUIZ, textvariable=var_quiz_label)
        var_quiz_label.set('Question')
        quiz_label.pack(side=tk.RIGHT, fill=tk.X)
        
        # Init Editor Frame
        EDIT.pack(side=tk.RIGHT, fill=tk.X)
        var_edit_label = tk.StringVar()
        edit_label = tk.Label(EDIT, textvariable=var_edit_label)
        var_edit_label.set('Editor')
        edit_label.pack(side=tk.TOP, fill=tk.X)
        # new question
        new_question_label = tk.Label(EDIT, text='Enter question text below:')
        new_question_label.pack(side=tk.TOP, fill=tk.X)
        new_question_entry = tk.Text(EDIT, font=5, width= 25, height=5)
        new_question_entry.pack(side=tk.TOP,fill=tk.X)
        
        new_answer_label = tk.Label(EDIT, text='Enter correct answer text below:')
        new_answer_label.pack(side=tk.TOP, fill=tk.X)
        new_answer_entry = tk.Entry(EDIT, font=5, width= 25)
        new_answer_entry.pack(side=tk.TOP,fill=tk.X)

        new_wrong1_label = tk.Label(EDIT, text='Enter first wrong answer text below:')
        new_wrong1_label.pack(side=tk.TOP, fill=tk.X)
        new_wrong1_entry = tk.Entry(EDIT, font=5, width= 25)
        new_wrong1_entry.pack(side=tk.TOP,fill=tk.X)

        new_wrong2_label = tk.Label(EDIT, text='Enter second wrong answer text below:')
        new_wrong2_label.pack(side=tk.TOP, fill=tk.X)
        new_wrong2_entry = tk.Entry(EDIT, font=5, width= 25)
        new_wrong2_entry.pack(side=tk.TOP,fill=tk.X)
        
        button_submit_question = tk.Button(EDIT, text='Save Question', bg='grey')
        button_submit_question.pack(side=tk.BOTTOM, fill=tk.X)
        cls._top.mainloop()

Gui.run()