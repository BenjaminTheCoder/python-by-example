from tkinter import *
from tkinter import messagebox
from random import randint
import csv



FILENAME = "name_gender_list.csv"

    
def Click():
    name = f'{entry_box.get()},{selectgender.get()}'
    
    listbox.insert(END, name)
    entry_box.delete(0, END)
    
def save():
    tmp_list = listbox.get(0, END)
    tmp_list = list(map(lambda name: name.split(','), tmp_list))
##    print('tmp_list', tmp_list)
    file = open(FILENAME, 'w', newline='')
    csvwriter = csv.writer(file) 
    csvwriter.writerows(tmp_list)
    file.close()
    file = open(FILENAME)
    print(file.read())
    file.close()


##ben,male
##kima,female
##kye,prefer not to say
##Bob,other
        
window = Tk()
window.title('My Window')
window.geometry('900x900')
window.wm_iconbitmap('icon.ico')

label = Label(text = 'Enter a name.')
label.pack()
entry_box = Entry (text = 0)
entry_box.pack()

selectgender = StringVar(window)
selectgender.set('Select a gender!!!')
genderlist = OptionMenu(window,selectgender,'male','female','other','prefer not to say')
genderlist.pack()

listbox = Listbox()
listbox.pack()

button = Button(text='Click me!', command=Click)
button.pack()

savebutton = Button(text='save', command=save)
savebutton.pack()
