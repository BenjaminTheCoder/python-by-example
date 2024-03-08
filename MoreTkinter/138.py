from tkinter import *
from tkinter import messagebox
from random import randint
import csv


    
def click(image):
    if image == 'spartan_shield.gif':
        photo = PhotoImage(file ='spartan_shield.gif')
        photobox.image = photo
        photobox['image'] = photo
        photobox.update()
    elif image == 'spartan_spear.gif':
        photo = PhotoImage(file ='spartan_spear.gif')
        photobox.image = photo
        photobox['image'] = photo
        photobox.update()
    elif image == 'spartan_sword.gif':
        photo = PhotoImage(file ='spartan_sword.gif')
        photobox.image = photo
        photobox['image'] = photo
        photobox.update()
    elif image == 'spartan_warrior.gif':
        photo = PhotoImage(file ='spartan_warrior.gif')
        photobox.image = photo
        photobox['image'] = photo
        photobox.update()
    elif image == 'spartan_helmet.gif':
        photo = PhotoImage(file ='spartan_helmet.gif')
        photobox.image = photo
        photobox['image'] = photo
        photobox.update()

def click2(image):
    photo = PhotoImage(file = f'spartan_{image}.gif')
    photobox.image = photo
    photobox['image'] = photo
    photobox.update()


        
window = Tk()
window.title('My Window')
window.geometry('900x900')
window.wm_iconbitmap('icon.ico')

photo = PhotoImage(file ='spartan_sword.gif')
photobox = Label(image = photo)
photobox.image = photo
photobox.pack()

selectimage = StringVar(window)
selectimage.set('SELECT IMAGE!!!!!')
imagelist = OptionMenu(window,selectimage,'shield','spear','warrior','sword','helmet', command=click2)
imagelist.pack()

##button = Button(text='Click me!', command=click)
##button.pack()

