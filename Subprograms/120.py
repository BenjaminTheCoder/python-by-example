import random

def answercheck(useranswer, correctanswer):
    if useranswer == correctanswer:
        print(f'you got it right the answer was {correctanswer}!!!')
    else:
        print(f'incorrect the answer was {correctanswer}!!!')

                
def adding():
    num1 = random.randint(5, 20)
    num2 = random.randint(5, 20)
    correctanswer = num1 + num2
    useranswer = int(input(f'What is {num1} + {num2} ? '))
    return (useranswer, correctanswer)

def subtracting():
    num1 = random.randint(25, 50)
    num2 = random.randint(1, 25)
    correctanswer = num1 - num2
    useranswer = int(input(f'What is {num1} - {num2} ? '))
    return (useranswer, correctanswer)

def multiplying():
    num1 = random.randint(2, 12)
    num2 = random.randint(2, 12)
    correctanswer = num1 * num2
    useranswer = int(input(f'What is {num1} × {num2} ? '))
    return (useranswer, correctanswer)

def dividing():
    num1 = random.randint(2, 10)
    num2 = random.randint(2, 10)
    multanswer = num1 * num2
    correctanswer = num2
    useranswer = int(input(f'What is {multanswer} ÷ {num1} ? '))
    return (useranswer, correctanswer)

def main():
    num = int(input('''
1) Addition
2) Subtraction
3) Multiplication
4) Division
Enter 1, 2, 3, or 4
'''))

    if num == 1:
        useranswer, correctanswer = adding()
        answercheck(useranswer, correctanswer)
    elif num == 2:
        useranswer, correctanswer = subtracting()
        answercheck(useranswer, correctanswer)
    elif num == 3:
        useranswer, correctanswer = multiplying()
        answercheck(useranswer, correctanswer)
    elif num == 4:
        useranswer, correctanswer = dividing()
        answercheck(useranswer, correctanswer)
    else:
        print('NEXT TIME ENTER 1, 2, 3, OR 4, LOSER!!!')

main()
