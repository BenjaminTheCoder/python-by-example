from tkinter import *
from tkinter import messagebox
from random import randint
import csv





    
def click(color):
    window.configure(bg = color)


        
window = Tk()
window.title('My Window')
window.geometry('900x900')
window.wm_iconbitmap('icon.ico')

selectcolor = StringVar(window)
selectcolor.set('SELECT COLOR!!!!!')
colorslist = OptionMenu(window,selectcolor,'red','white','blue','yellow','green', command=click)
colorslist.pack()

##button = Button(text='Click me!', command=click)
##button.pack()

