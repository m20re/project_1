from tkinter import *
from random import randrange, choice
import csv


class GUI:
    def __init__(self, window):

        
        self.window = window
        
        #title frame
        self.frame_title = Frame(self.window)
        self.label_title = Label(self.frame_title, font=("Arial",25), text="Math Checker")
        self.label_title.pack()
        self.frame_title.pack(pady=10)






