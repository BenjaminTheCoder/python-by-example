from tkinter import *
from tkinter import messagebox


def Click():
    num = entry_box.get()
    if num.isdigit():
        listbox.insert(END, num)
    else:
        entry_box.delete(0, END)


def reset():
    listbox.delete(0, END)
    entry_box.delete(0, END)
        

window = Tk()
window.title('My Window')
window.geometry('600x600')    



label = Label(text = 'Enter a whole number.')
label.pack()

entry_box = Entry (text = 0)
entry_box.pack()

button = Button(text='Click me!', command=Click)
button.pack()


listbox = Listbox()
listbox.pack()

resetcallback = Button(text='Reset button!', command=reset)
resetcallback.pack()
window.mainloop()
