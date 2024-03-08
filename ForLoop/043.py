answer = input('Do you want to count up or down? ')
if answer == 'up':
    num = int(input('what is the top number? '))
    for i in range(1,num+1):   
        print(i)
elif answer == 'down':
    num = int(input('enter a number below 20. '))
    for i in range(20,num-1,-1):
        print(i)
else:
    print('A what?')
              
 
