from tkinter import *
from tkinter import messagebox
from random import randint


dice = ['⚀','⚁','⚂','⚃','⚄','⚅']
# dice = '⚀ ⚁ ⚂ ⚃ ⚄ ⚅'.split()

def click():
    die = randint(0, 5)
    die2 = randint(0, 5)
    output_box.config(text = dice[die])
    output_box2.config(text = dice[die2])
    if die == 0 and die2 == 0:
        messagebox.showinfo("Snake eyes", 'Snake Eyes!!!')
    if die == 1 and die2 == 1:
        messagebox.showinfo("Four eyes", 'Four Eyes!!!')


window = Tk()
window.title('My Window')
window.geometry('600x600')    

button = Button(text='Roll the die!!!', command=click)
button.pack() 

output_box = Message(text = "", bg='lightgreen', font=('Comic Sans MS', 100, 'bold'))
output_box.pack()

output_box2 = Message(text = "", bg='lightblue', font=('Comic Sans MS', 100, 'bold'))
output_box2.pack()

##
##label = Label(text = 'What is your name?')
##label.pack()
##
##entry_box = Entry (text = 0)
##entry_box.pack()



window.mainloop()
