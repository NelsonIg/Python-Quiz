# -*- coding: utf-8 -*-
''' Graphical User Interface for EduQuiz'''
import tkinter as tk

class TopGui(tk.Frame):

    def __init__(self):
        master = tk.Tk()
        super().__init__(master)
        #self.master = master

        
    def run(self):
        #init Menu
        self.master.resizable(0,0)
        self.master.title('Menu')
        self.buttonGame = tk.Button(self.master, text='Start Quiz', width=20,
                                    height = 10, bg='orange',activebackground ='olivedrab2',
                                    bd = 4, font = ('arial','10','bold'))
        self.buttonGame.pack(side=tk.LEFT)
        
        self.buttonEditor = tk.Button(self.master, text='Enter Editor', width=20,
                                      height = 10, bg='olivedrab1', activebackground ='olivedrab2',
                                      bd = 4, font = ('arial','10','bold'))
        self.buttonEditor.pack(side=tk.RIGHT)
        self.mainloop()
        

class Editor(tk.Frame):
    def __init__(self):
        master = tk.Tk()
        super().__init__(master)

    def save_question(self):
        self.master.destroy()
        print('start quiz\nclose menu')
        
        
    def run(self):
        #init Menu
        self.master.resizable(0,0)
        self.master.title('Menu')
        self.button_save_q = tk.Button(self.master, text='Save Question',
                                    width=20, height = 10, command=self.save_question,
                                    bg='orange',activebackground ='olivedrab2',
                                    bd = 4, font = ('arial','10','bold'))
        self.button_exit = tk.Button(self.master, text='Save Question',
                                    width=20, height = 10, command=self.master.destroy,
                                    bg='orange',activebackground ='olivedrab2',
                                    bd = 4, font = ('arial','10','bold'))
        self.button_exit.pack(side=tk.LEFT)
        self.mainloop()
# class GameGui:

top = TopGui()
top.run()
edit = Editor()
edit.run()