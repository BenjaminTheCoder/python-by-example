from tkinter import *
from tkinter import messagebox
from random import randint


BGCOLOR = 'lightblue'
FONT = 'Comic Sans MS'
FONTSIZE = 100
KM_MI = 1.6093
MI_KM = 0.6214


def button1_callback():
    num = entry_box.get()
    response = round(KM_MI * float(num),3)
    outputbox.config(text = response, bg = BGCOLOR, font=(FONT, FONTSIZE, 'bold'))
    

def button2_callback():
    num = entry_box.get()
    response = round(MI_KM * float(num),3)
    outputbox.config(text = response, bg = BGCOLOR, font=(FONT, FONTSIZE, 'bold'))
    

window = Tk()
window.title('My Window')
window.geometry('600x600')
window.configure(bg=BGCOLOR)


entry_box = Entry(text = '')
entry_box.pack()

button1 = Button(text='km to miles', command=button1_callback)
button1.pack()

button2 = Button(text='miles to km', command=button2_callback)
button2.pack()

outputbox = Message(text = '', width=500)
outputbox.pack()



window.mainloop()
