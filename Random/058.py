import random
score = 0
for i in range(5):
    print(f'score = {score}')
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    answer = num1 * num2
    #print(answer)
    response = int(input(f'what is {num1}*{num2}? '))
    if response == answer:
        score += 1
print(f'score = {score}')
print('thank you for playing!')
    

    

    


    

    


































































































































































































































































































































