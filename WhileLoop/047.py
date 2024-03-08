total = 0
response = 'y'
while response == 'y':
    num = int(input('enter a number: '))
    total = total + num
    response = input('do you want to add another number? ')
print(f'The total is {total}')
