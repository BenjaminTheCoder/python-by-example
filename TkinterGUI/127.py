from tkinter import *
from tkinter import messagebox
from random import randint

names = []


def click():
    global names
    name = str(entry_box.get())
    names.append(name)
    outputbox.config(text = str(names))

def reset():
    global names
    entry_box.delete(0, END)
    names = []
    outputbox.config(text = str(names))
    

window = Tk()
window.title('My Window')
window.geometry('600x600')

label = Label(text = 'Enter a name.')
label.pack()

entry_box = Entry (text = 0)
entry_box.pack()

button = Button(text='Click me!', command=click)
button.pack()

outputbox = Message(text = str(names))
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
