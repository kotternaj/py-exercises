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

        # Buttons 7, 8, 9
        self.button1 = Button(self, bg = "#98dbc6", bd =12,
        text="7", padx = 33, pady = 25, font=("Helvetica", 20, "bold"),
        command = lambda : self.buttonClick(7))
        self.button1.grid(row = 2, column = 0, sticky = W)

        self.button2 = Button(self, bg = "#98dbc6", bd =12,
        text="8", padx = 33, pady = 25, font=("Helvetica", 20, "bold"),
        command = lambda : self.buttonClick(8))
        self.button2.grid(row = 2, column = 1, sticky = W)

        self.button3 = Button(self, bg = "#98dbc6", bd =12,
        text="9", padx = 33, pady = 25, font=("Helvetica", 20, "bold"),
        command = lambda : self.buttonClick(9))
        self.button3.grid(row = 2, column = 2, sticky = W)
        
        # Buttons 4, 5, 6
        self.button4 = Button(self, bg = "#98dbc6", bd =12,
        text="4", padx = 33, pady = 25, font=("Helvetica", 20, "bold"),
        command = lambda : self.buttonClick(4))
        self.button4.grid(row = 3, column = 0, sticky = W)

        self.button5 = Button(self, bg = "#98dbc6", bd =12,
        text="5", padx = 33, pady = 25, font=("Helvetica", 20, "bold"),
        command = lambda : self.buttonClick(5))
        self.button5.grid(row = 3, column = 1, sticky = W)

        self.button6 = Button(self, bg = "#98dbc6", bd =12,
        text="6", padx = 33, pady = 25, font=("Helvetica", 20, "bold"),
        command = lambda : self.buttonClick(6))
        self.button6.grid(row = 3, column = 2, sticky = W)

        # Buttons 1, 2, 3
        self.button7 = Button(self, bg = "#98dbc6", bd =12,
        text="1", padx = 33, pady = 25, font=("Helvetica", 20, "bold"),
        command = lambda : self.buttonClick(1))
        self.button7.grid(row = 4, column = 0, sticky = W)

        self.button8 = Button(self, bg = "#98dbc6", bd =12,
        text="2", padx = 33, pady = 25, font=("Helvetica", 20, "bold"),
        command = lambda : self.buttonClick(2))
        self.button8.grid(row = 4, column = 1, sticky = W)

        self.button9 = Button(self, bg = "#98dbc6", bd =12,
        text="3", padx = 33, pady = 25, font=("Helvetica", 20, "bold"),
        command = lambda : self.buttonClick(3))
        self.button9.grid(row = 4, column = 2, sticky = W)
        
        # 0 and arithmetic operators
        self.button10 = Button(self, bg = "#98dbc6", bd =12,
        text="0", padx = 33, pady = 25, font=("Helvetica", 20, "bold"),
        command = lambda : self.buttonClick(0))
        self.button10.grid(row = 5, column = 0, sticky = W)

        self.Addbutton = Button(self, bg = "#98dbc6", bd =12,
        text="+", padx = 36, pady = 25, font=("Helvetica", 20, "bold"),
        command = lambda : self.buttonClick('+'))
        self.Addbutton.grid(row = 2, column = 3, sticky = W)

        self.Subbutton = Button(self, bg = "#98dbc6", bd =12,
        text="-", padx = 39, pady = 25, font=("Helvetica", 20, "bold"),
        command = lambda : self.buttonClick('-'))
        self.Subbutton.grid(row = 3, column = 3, sticky = W)

        self.Multbutton = Button(self, bg = "#98dbc6", bd =12,
        text="*", padx = 38, pady = 25, font=("Helvetica", 20, "bold"),
        command = lambda : self.buttonClick('*'))
        self.Multbutton.grid(row = 4, column = 3, sticky = W)

        self.Divbutton = Button(self, bg = "#98dbc6", bd =12,
        text="/", padx = 33, pady = 25, font=("Helvetica", 20, "bold"),
        command = lambda : self.buttonClick('/'))
        self.Divbutton.grid(row = 5, column = 3, sticky = W)

        self.Equalbutton = Button(self, bg = "#e6d72a", bd =12,
        text="=", padx = 100, pady = 25, 
        command = self.CalculateTask, font=("Helvetica", 20, "bold"))
        self.Equalbutton.grid(row = 5, column = 1, sticky = W, columnspan = 2)

        self.Clearbutton = Button(self, bg = "#e6d72a", bd =12,
        text="AC", padx = 7, width= 28, font=("Helvetica", 20, "bold"),
        command = self.ClearDisplay)
        self.Clearbutton.grid(row = 1, columnspan = 4, sticky = W)

    def buttonClick(self, number):
        self.task = str(self.task) + str(number)
        self.UserIn.set(self.task)

    def CalculateTask(self):
        self.data = self.user_input.get()
        try:
            self.answer = eval(self.data)
            self.displayText(self.answer)
            self.task = self.answer
        except SyntaxError as e:
            self.displayText("Invalid Syntax")
            self.task = ''
    
    def displayText(self, value):
        self.user_input.delete(0, END)
        self.user_input.insert(0, value)

    def ClearDisplay(self):
        self.task = ''
        self.user_input.delete(0, END)
        self.user_input.insert(0, 'O')

calculator = Tk()

calculator.resizable(width = False, height = False)
app = Application(calculator)
calculator.mainloop()