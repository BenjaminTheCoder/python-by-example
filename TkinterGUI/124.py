from tkinter import *
from tkinter import messagebox


def click():
    name = entry_box.get()
    messagebox.showinfo("hello", f'Hello {name}!')


window = Tk()
window.title('My Window')
window.geometry('300x200')

label = Label(text = 'What is your name?')
label.pack()

entry_box = Entry (text = 0)
entry_box.pack()

button = Button(text='Click me!', command=click)
button.pack()


window.mainloop()
