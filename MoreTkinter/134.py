from tkinter import *
from tkinter import messagebox
from random import randint
import csv


def reset():
    global answer
    num1 = randint(10,50)
    num2 = randint(10,50)
    answer = num1 + num2
    label.config(text = f'What is {num1} + {num2} ?')

    
def click():
    uanswer = int(entry_box.get())
    if uanswer == answer:
        photo = PhotoImage(file ='checkmark.gif')
        photobox.image = photo
        photobox['image'] = photo
    else:
        photo = PhotoImage(file ='x.gif')
        photobox.image = photo
        photobox['image'] = photo
        photobox.update()

        
window = Tk()
window.title('My Window')
window.geometry('900x900')
window.wm_iconbitmap('icon.ico')

num1 = randint(10,50)
num2 = randint(10,50)
answer = num1 + num2


label = Label(text = f'What is {num1} + {num2} ?')
label.pack()

entry_box = Entry()
entry_box.pack()

button = Button(text='Click me!', command=click)
button.pack()

photo = PhotoImage(file ='logo.gif')
photobox = Label(image = photo)
photobox.image = photo
photobox.pack()

resetcallback = Button(text='Reset button!', command=reset)
resetcallback.pack()
window.mainloop()
