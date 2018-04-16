import sys
from tkinter import *

def TimesTable():
    print('\n')
    for x in range(1, 13):
        m = int(EnterTable.get())
        print('t', (x), ' x ', (m), '=', (x * m,))

Multiply = Tk()
Multiply.geometry('250x250+700+200')
Multiply.title('Multiplication Table')

EnterTable=StringVar()

label1=Label(Multiply, text='Mult Times Table', font=30, fg='Black').grid(row=1,column=6)
label1=Label(Multiply, text='                                 ').grid(row=2, column=6)

Multiply.mainloop()

