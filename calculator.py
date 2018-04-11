from tkinter import *

class Application(Frame):
    ''' Main class for calculator '''

    def __init__(self, master):
        ''' Initialize the Frame '''
        super (Application, self).__init__(master)
        self.task=""
        self.UserIn = StringVar()
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        ''' Create the buttons for the calculator'''
        # User input stored as an Entry widget 

        self.user_input = Entry(self, bg = "#5bc8AC", bd = 29,
        insertwidth = 4, width = 24,
        font = ("Verdana", 20, "bold"), textvariable = self.UserIn, justify= RIGHT)
        self.user_input.grid(columnspan = 4)

        self.user_input.insert(0, "0")

        self.button1 = Button(self, bg = "#98dbc6", bd =12,
        text="7", padx = 33, pady = 25, font=("Helvetica", 20, "bold"),
        command = lambda : self.buttonClick(7))
        self.button1.grid(row = 2, column = 0, sticky = W)


calculator = Tk()

calculator.resizable(width = False, height = False)
app = Application(calculator)
calculator.mainloop()