from tkinter import *
from tkinter import ttk
from tkinter import font
import time
import datetime

global endTime

def quit(*args):
    root.destroy()

def cant_wait():
   timeLeft = endTime - datetime.datetime.now()
   timeLeft = timeLeft - date.timedelta(microseconds=timeLeft.microseconds)

   txt.set(timeLeft)

   root.after(1000.cant_wait)

   