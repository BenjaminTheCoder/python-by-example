from tkinter import *
from tkinter import messagebox
import csv


FILENAME = "people.csv"
file = open(FILENAME, 'a', newline='')
file.close()




def reset():
    listbox.delete(0, END)
    entry_box2.delete(0, END)
    entry_box.delete(0, END)


def save():
    file = open(FILENAME, 'a', newline='')
    age = entry_box2.get()
    name = entry_box.get()
    file.write(f'{name},{age}\n')
    file.close()



def loadcsv():
    file = open(FILENAME)
    lines = file.readlines()
    for line in lines:
        listbox.insert(END, line)
    file.close()
        

window = Tk()
window.title('My Window')
window.geometry('600x600')    



label = Label(text = 'Enter a name.')
label.pack()

entry_box = Entry()
entry_box.pack()

label2 = Label(text = 'Enter a age.')
label2.pack()

entry_box2 = Entry()
entry_box2.pack()



button = Button(text='Click me!', command=save)
button.pack()



listbox = Listbox()
listbox.pack()


button2 = Button(text='load csv', command=loadcsv)
button2.pack()






resetcallback = Button(text='Reset button!', command=reset)
resetcallback.pack()
window.mainloop()
