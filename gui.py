from tkinter import *
from random import randrange, choice


class GUI:
    def __init__(self, window) -> None:
        """
        Defines six seperate frames: title, num_1 & 2,
         equation, results, new equation, and check answer.
        :return: none
        """

        self.window = window

        # title frame
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

        self.entry_answer = Entry(self.frame_equation, font=("Arial", 25), width=5)
        
        self.frame_equation.pack(pady=5)

        # results frame
        self.frame_results = Frame(self.window)
        self.intended_result = StringVar()
        self.intended_results_label = Label(self.frame_results, textvariable=self.intended_result, font=("Arial", 12))

        self.intended_results_label.pack_forget()
        self.frame_results.pack(pady=10, anchor='s')

        # new equation frame
        self.frame_generate_button = Frame(self.window)
        self.generate_button = Button(self.frame_generate_button, text='Generate Equation', command=self.generate_equation_and_result)
        self.generate_button.pack(padx=10)
        self.frame_generate_button.pack(anchor='sw',side=LEFT, pady=10)

        # check answer frame
        self.frame_check = Frame(self.window)
        self.button_check = Button(self.frame_check, text='Check Answer', command=self.check_answer)
        self.button_check.pack(padx=10)
        self.frame_check.pack(anchor="se", side=RIGHT, pady=10)

        

    def generate_equation_and_result(self) -> None:
        """
        Generates a two random numbers, and operation for those numbers.
        The operation will be displayed on the GUI itself, and written into
         output.txt
        :return: none 
        """
        self.intended_results_label.pack_forget()
        self.entry_answer.delete(0,END)

        num1 = randrange(0,20)
        num2 = randrange(1,9)
        operation = choice(['+', '-', '*'])

        self.number1.set(str(num1))
        self.number2.set(str(num2) + '    =')
        self.operation.set(operation)

        if operation == '+':
            self.result = num1 + num2
        elif operation == '-':
            self.result = num1 - num2
        else:
            self.result = num1 * num2
        
        self.label_num1.pack(padx=10, side=LEFT)
        self.label_operation.pack(padx=10, side=LEFT)
        self.label_num2.pack(padx=10, side=LEFT)
        self.entry_answer.pack(padx=10, side=LEFT)
        self.frame_equation.pack(pady=10)

        with open('output.txt', 'a') as f:
            if operation == '+':
                f.write(f'{num1} + {num2} = {self.result}\n')
            elif operation == '-':
                f.write(f'{num1} - {num2} = {self.result}\n')
            else:
                f.write(f'{num1} * {num2} = {self.result}\n')
        return

    
    def check_answer(self) -> None:
        """
        Checks whether a person has correctly answered the equation.
        The GUI will respond depending on whether it's right, wrong
         or if the input is invalid.
        :return: none
        """

        try:
            if float(self.entry_answer.get().strip()) == self.result:
                self.intended_result.set('Correct! Generate a new equation!')
                self.intended_results_label.pack(padx=5)
            else:
                self.intended_result.set('Incorrect! Try again or make a new equation!')
                self.intended_results_label.pack(padx=5)
        except ValueError:
            self.intended_result.set("Input only whole numbers!")
            self.intended_results_label.pack(padx=5)
        return
