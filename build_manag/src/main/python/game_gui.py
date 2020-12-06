# -*- coding: utf-8 -*-
''' Graphical User Interface for EduQuiz'''
import tkinter as tk
import game_data as gd
import random as rd

class Gui:
    _top = tk.Tk()
    _top.resizable(0,0)
    _quiz_frame = tk.Frame(_top, bg='grey')
    _edit_frame = tk.Frame(_top, bg='blue')
    
    
    def verify(self):
        user_inp = self.quiz_user_inp.get()
        self.q.set_user_answer(user_inp)
        self.quiz_console.insert(tk.INSERT, '\n'+str(self.q.verify()))
    
    def next_question(self):
        self.quiz_console.delete(1.0, tk.END)
        questions = gd.load_question('questions.csv', 6)
        self.q = rd.choice(questions)
        self.quiz_console.insert(1.0, self.q.get_text())
        
       
    def write_Question(self):
        q_type = 'QandA'
        text = self.new_question_entry.get()
        answer = self.new_answer_entry.get()
        gd.write_q2csv('questions.csv', q_type, text, answer)
        self.new_question_entry.delete(0, tk.END)
        self.new_answer_entry.delete(0, tk.END)
        
    
    def run(self):
        # Two Frames
        EDIT = self._edit_frame
        QUIZ = self._quiz_frame
        TOP = self._top
        # Load Question
        self.button_next_question = tk.Button(TOP, text='Next Question',
                                       command= self.next_question, bg='grey')
        self.button_next_question.grid(row=0, column=1)
        # Init Quiz Frame
        QUIZ.grid(row=0, column=0)
        var_quiz_label = tk.StringVar()
        self.quiz_label = tk.Label(QUIZ, textvariable=var_quiz_label)
        var_quiz_label.set('Question')
        self.quiz_label.pack(side=tk.TOP, fill=tk.X)
        # Consol
        self.var_consol = tk.StringVar()
        self.quiz_console = tk.Text(QUIZ, width=25, height=5)
        self.quiz_console.pack(side=tk.TOP, fill=tk.X)
        # User Input
        self.quiz_inp_label = tk.Label(QUIZ, text='Enter answer below:')
        self.quiz_inp_label.pack(side=tk.TOP, fill=tk.X)        
        self.quiz_user_inp = tk.Entry(QUIZ, width=25)
        self.quiz_user_inp.pack(side=tk.TOP, fill=tk.X)
        self.button_verify = tk.Button(QUIZ, text='Enter',command=self.verify, bg='grey')
        self.button_verify.pack(side=tk.TOP, fill=tk.X)
        
        # Init Editor Frame
        EDIT.grid(row=0, column=2)
        var_edit_label = tk.StringVar()
        self.edit_label = tk.Label(EDIT, textvariable=var_edit_label)
        var_edit_label.set('Editor')
        self.edit_label.pack(side=tk.TOP, fill=tk.X)
        # new question
        self.new_question_label = tk.Label(EDIT, text='Enter question text below:')
        self.new_question_label.pack(side=tk.TOP, fill=tk.X)
        self.new_question_entry = tk.Entry(EDIT, font=5, width= 25)
        self.new_question_entry.pack(side=tk.TOP,fill=tk.X)
        
        self.new_answer_label = tk.Label(EDIT, text='Enter correct answer text below:')
        self.new_answer_label.pack(side=tk.TOP, fill=tk.X)
        self.new_answer_entry = tk.Entry(EDIT, font=5, width= 25)
        self.new_answer_entry.pack(side=tk.TOP,fill=tk.X)

        
        self.button_submit_question = tk.Button(EDIT, text='Save Question',
                                               command= self.write_Question, bg='grey')
        self.button_submit_question.pack(side=tk.BOTTOM, fill=tk.X)
        self._top.mainloop()
quiz = Gui()
quiz.run()