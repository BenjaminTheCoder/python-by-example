from tkinter import *
#from tkinter import messagebox
import json

FILENAME = "Grades.json"

data = json.load(open(FILENAME))

def save():
    json.dump(data, open(FILENAME, 'w'), indent=2)



def reset():
    entry_box2.delete(0, END)
    entry_box.delete(0, END)



def Add():
    # Load the Grades.json file
    # Assign the student name to a variable
    # Assign the grade to a int variable
    # Assign the student name as a key
    # in the dictionary and the grade as the value
    # Save the dictionary in the Grades.json file
    name = entry_box.get()
    grade = int(entry_box2.get())
    data[name] = grade
    save()
    
    
    
    

   
    
    
    
    
    
    
        

window = Tk()
window.title('My Window')
window.geometry('600x600')    



label = Label(text = 'Enter a name.')
label.pack()

entry_box = Entry()
entry_box.pack()

label2 = Label(text = 'Enter a grade.')
label2.pack()

entry_box2 = Entry()
entry_box2.pack()










button2 = Button(text='Add', command=Add)
button2.pack()






resetcallback = Button(text='Clear', command=reset)
resetcallback.pack()
window.mainloop()
