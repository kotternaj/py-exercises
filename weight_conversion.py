from tkinter import *
from tkinter import ttk

root = Tk()
root.title('Meters to Feet')

mainframe = ttk.Frame(root, padding='3 3 12 12')
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

feet = StringVar()
feet = StringVar()

feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet)
feet_entry.grid(column=2, row=1, sticky=(W, E))

ttk.Label(mainframe, textvariable=meters).grid(colum=2, row=2, sticky=(W, E))
ttk.Button(mainframe, text='Calculate', command=calcuate).grid(column=3, row=3, sticky=W)

