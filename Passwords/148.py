import json
from pprint import pprint
from tabulate import tabulate
from operator import itemgetter
import string

FILENAME = "Acounts.json"


# CRUD = Typical database program
# Create - add()
# Retrieve - Find()
# Update - Edit() # TODO!!
# Delete - Delete

data = json.load(open(FILENAME))

def save():
    json.dump(data, open(FILENAME, 'w'), indent=2)

def view(rows):
    print(tabulate(rows, headers="keys"))

def casecheck(password, char_list):
    contains = False
    for char in password:
        if char in char_list:
            return True

    return contains

def password_manager():
    points = 0
    while points <= 2:
        password = input('Enter a password. ')
        if len(password) >= 8:
            points += 1
        if casecheck(password,string.ascii_uppercase):
            points += 1
        if casecheck(password,string.ascii_lowercase):
            points += 1
        if casecheck(password,string.punctuation):
            points += 1
        if casecheck(password,string.digits):
            points += 1
        if casecheck(password,string.whitespace):
            points = 0
        if points <= 2:
            print('It is a weak password try again.')
    if points == 3 or points == 4:
        print('This password can be improved. ')
    if points == 5:
        print('This is a strong password. ')
    return password

def create_file():
    user_name = input('Enter a username. ')
    password = password_manager()
    data[user_name] = password
    save()
    
def change_password():
    user_name = input('Enter your username. ')
    if user_name in data:
        print('Valid username.')
    else:
        print('Invalid user name.')
        main()

    password = password_manager()
    data[user_name] = password
    save()
    
def show_user_names():
    print('\n'.join(data.keys()))
        
     
    
    
def main():
    num = int(input('''
1) Create a new user ID
2) Change a password
3) Display user IDs
4) Quit
'''))

    match num:
        case 1:
            create_file()
        case 2:
            change_password()
        case 3:
            show_user_names()
        case 4:
            quit()
        case _:
            print("Invalid case!")
    main()
    

main()

