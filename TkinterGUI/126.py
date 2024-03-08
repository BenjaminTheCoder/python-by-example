from tkinter import *
from tkinter import messagebox
from random import randint

total = 0


def click():
    global total
    number = float(entry_box.get())
    total += number
    outputbox.config(text = total)

def reset():
    global total
    entry_box.delete(0, END)
    outputbox['text'] = 0
    total = 0
    
    
    

window = Tk()
window.title('My Window')
window.geometry('600x600')

label = Label(text = 'Enter a number.')
label.pack()

entry_box = Entry (text = 0)
entry_box.pack()

button = Button(text='Click me!', command=click)
button.pack()

outputbox = Message(text = total)
outputbox.pack()

resetbutton = Button(text='reset button', command=reset)
resetbutton.pack()







##
##label = Label(text = 'What is your name?')
##label.pack()
##
##entry_box = Entry (text = 0)
##entry_box.pack()



window.mainloop()
