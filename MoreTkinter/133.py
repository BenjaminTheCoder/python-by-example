from tkinter import *
from tkinter import messagebox
import csv







def reset():
    entry_box.delete(0, END)
    entrybox.delete(0, END)
    
def Click():
    entrybox.delete(0, END)
    entrybox.insert(0, f'Hello {entry_box.get()}!!')
    
        

window = Tk()
window.title('My Window')
window.geometry('600x600')
window.wm_iconbitmap('icon.ico')

logo = PhotoImage(file ='logo.gif')
logoimage = Label(image = logo)
logoimage.pack()

label = Label(text = 'Enter a name.')
label.pack()

entry_box = Entry()
entry_box.pack()

button = Button(text='Click me!', command=Click)
button.pack()

entrybox = Entry(text = '')
entrybox.pack()

resetcallback = Button(text='Reset button!', command=reset)
resetcallback.pack()
window.mainloop()
