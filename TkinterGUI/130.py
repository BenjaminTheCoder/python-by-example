from tkinter import *
from tkinter import messagebox
import csv


FILENAME = "num_list.csv"


def Click():
    num = entry_box.get()
    if num.isdigit():
        listbox.insert(END, num)
    else:
        entry_box.delete(0, END)


def reset():
    listbox.delete(0, END)
    entry_box.delete(0, END)


def save():
    tmp_list = listbox.get(0, END)
    tmp_list = list(map(lambda num: [num], tmp_list))
    print('tmp_list', tmp_list)
    file = open(FILENAME, 'w', newline='')
    csvwriter = csv.writer(file) 
    csvwriter.writerows(tmp_list)
    file.close()
        

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


savebutton = Button(text='Save to csv.', command=save)
savebutton.pack()



resetcallback = Button(text='Reset button!', command=reset)
resetcallback.pack()
window.mainloop()
