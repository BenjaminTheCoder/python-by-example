import json
from pprint import pprint
from tabulate import tabulate
from operator import itemgetter


# CRUD = Typical database program
# Create - add()
# Retrieve - Find()
# Update - Edit() # TODO!!
# Delete - Delete

data = json.load(open('phonebook.json'))

def save():
    json.dump(data, open('phonebook.json', 'w'), indent=2)

def view(rows):
    print(tabulate(rows, headers="keys"))

def add():
    IDs = []
    for row in data['Names']:
        IDs.append(row['ID'])

##    IDs = list(map(lambda row: row['ID'], data['Names']))
##    IDs = list(map(itemgetter('ID'), data['Names']))
##    IDs = [row['ID'] for row in data['Names']]
        
    new_ID = max(IDs)+1
##    print(new_ID)

    firstName = input('Enter a first name.')
    surname = input('Enter a surname.')
    phoneNumber = input('Enter a phone number.')
    newPerson = {'ID': new_ID, 'First Name': firstName, 'Surname': surname, 'Phone Number': phoneNumber}
    data['Names'].append(newPerson)

    save()
    view(data['Names'])

def Edit():
    view(data['Names'])
    ID = int(input('enter an ID.'))
    index = -1
    for i in range(len(data['Names'])):
        row = data['Names'][i]
        if row['ID'] == ID:
            index = i
            break
        
    if index == -1:
        print('invalid index')
        return

    row = data['Names'][index]
    firstName = input('Enter a first name.')
    surname = input('Enter a surname.')
    phoneNumber = input('Enter a phone number.')
    newPerson = {'ID': ID, 'First Name': firstName, 'Surname': surname, 'Phone Number': phoneNumber}
    data['Names'][index] = newPerson     
    view(data['Names'])
    save()


def Find():
    view(data['Names'])
    name = input('enter a surname.')
    filtered_surnames = []
    for row in data['Names']:
        if row['Surname'] == name:
            filtered_surnames.append(row)
    view(filtered_surnames)

def my_filter(predicate, values):
    new_values = []
    for value in values:
        if predicate(value):
            new_values.append(value)
    return new_values

def Find2():
    view(data['Names'])
    name = input('enter a surname.')
    view(list(filter(lambda row: row['Surname'] == name, data['Names'])))
    # view([row for row in data['Names'] if row['Surname'] == name])
    
def Delete():
    view(data['Names'])
    ID = int(input('enter an ID.'))
    index = -1
    for i in range(len(data['Names'])):
        row = data['Names'][i]
        if row['ID'] == ID:
            index = i
            break
        
    if index == -1:
        print('invalid index')
        return

    del data['Names'][index]        
    view(data['Names'])
    save()
         
    
    
def main():
    num = int(input('''
1) View phone book
2) Add to phone book
3) Edit a person
4) Search for surname
5) Delete person from phone book
6) Quit
Enter your choice: 
'''))

    match num:
        case 1:
            view(data['Names'])
        case 2:
            add()
        case 3:
            Edit()
        case 4:
            Find()
        case 5:
            Delete()
        case 6:
            quit()
        case _:
            print("Invalid case!")
    main()
    

main()
