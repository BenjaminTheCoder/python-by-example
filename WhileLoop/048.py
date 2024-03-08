people = 0
response = 'y'
while response == 'y':
    person = input('Who do you want to invite? ')
    print(f'{person} has been invited.')
    people = people + 1
    response = input('do you want to invite another person? ')
print(f'You have invited {people} people')
