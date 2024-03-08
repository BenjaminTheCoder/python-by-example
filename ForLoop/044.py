num = int(input('How many people will be at the party? '))              
if num > 9:
    print('To many people!')
else:
    for i in range(num):
        name = input('Who is invited? ')
        print(f'{name} is invited to the party!')
