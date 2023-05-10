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

         # label num_1 & num_2 frame
        self.frame_num_display = Frame(self.window)
        self.label_num_1 = Label(self.frame_num_display, text=' First Number', font=("Arial", 8))
        self.label_num_2 = Label(self.frame_num_display, text=' Second Number', font=("Arial", 8))

        self.frame_num_display.pack(pady=5, anchor='w')

        # equation frame
        self.number1 = StringVar()
        self.number2 = StringVar()
        self.operation = StringVar()
    
        self.frame_equation = Frame(self.window)
        self.label_num1 = Label(self.frame_equation, font=("Arial", 25), textvariable=self.number1)
        self.label_operation = Label(self.frame_equation, font=("Arial", 25), textvariable=self.operation)
        self.label_num2 = Label(self.frame_equation, font=("Arial", 25), textvariable=self.number2)
        self.entry_answer = Entry(self.frame_equation, font=("Arial", 25), width=5)

        self.label_num1.pack_forget()
        self.label_operation.pack_forget()
        self.label_num2.pack_forget()
        self.entry_answer.pack_forget()
        self.entry_answer = Entry(self.frame_equation, font=("Arial", 25), width=5)
        
        self.frame_equation.pack(pady=5)

        # new equation button
        self.frame_generate_button = Frame(self.window)
        self.generate_button = Button(self.frame_generate_button, text='Generate Equation', command=self.generate_equation_and_result)
        self.generate_button.pack(padx=5)
        self.frame_generate_button.pack(anchor='s',pady=10) 

        

    def generate_equation_and_result(self) -> list:
        num1 = randrange(0,100)
        num2 = randrange(1,100)
        operation = choice(['+', '-', '*', '/'])

        self.number1.set(str(num1))
        self.number2.set(str(num2) + '    =')
        self.operation.set('*')

        if operation == '+':
            self.result = num1 + num2
        elif operation == '-':
            self.result = num1 - num2
        elif operation == '*':
            self.result = num1 * num2
        else:
            self.result = num1 / num2
        
        self.label_num1.pack(padx=10, side=LEFT)
        self.label_operation.pack(padx=10, side=LEFT)
        self.label_num2.pack(padx=10, side=LEFT)
        self.entry_answer.pack(padx=10, side=LEFT)
        self.frame_equation.pack(pady=10)
        return






