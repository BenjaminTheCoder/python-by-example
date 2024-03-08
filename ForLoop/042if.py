total = 0
for i in range(5):
    num = int(input('Enter a number. '))
    answer = input('do you want this number in the total? ')
    if answer == 'y':
        total += num

print(total)
