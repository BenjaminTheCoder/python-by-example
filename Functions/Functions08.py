# Write a function called main which takes no args.
# Ask the user for a number.
# Print "The factorial of num is: answer"


def add(num1, num2):   
    return num1 + num2

def mult(num1, num2):   
    total = 0
    for i in range(num1):
        total = add(total, num2)
    return total
   

def power(num1, num2):   
    total = 1
    for i in range(num2):
        total = mult(total, num1)
    return total

def fold(num1, num2, identity, operator):
    total = identity
    for i in range(num2):
        total = operator(total, num1)
    return total


def factorial(num):
    total = 1
    for i in range(1, num+1):
        total = mult(total, i)
    return total
        

def main():
    num = int(input('Enter a number: '))
    answer = factorial(num)
    print(f"The factorial of {num} is {answer}.")

    
main()




##factorial_anwser = factorial(5)
##print(factorial_anwser)
##factorial_anwser = factorial(3)
##print(factorial_anwser)
##factorial_anwser = factorial(7)
##print(factorial_anwser)









    
