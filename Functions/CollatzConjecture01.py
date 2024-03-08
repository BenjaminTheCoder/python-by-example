# Write a program that asks the user to enter a positive integer.
# Print the Collatz sequence and stop at 1. You can print as a column or with commas in between numbers.
# Use the isEven function. If it returns true, the number is even, otherwise it's odd.

def isEven(num):
    return num % 2 == 0

def main():

    x = int(input('Enter a number. '))
    while x != 1:
        if isEven(x) == True:
            x  = x // 2
        else:
            x = x * 3 + 1
        print(x, end=" ")

##def add(num1, num2):   
##    return num1 + num2
##
##def mult(num1, num2):   
##    total = 0
##    for i in range(num1):
##        total = add(total, num2)
##    return total
##   
##
##def power(num1, num2):   
##    total = 1
##    for i in range(num2):
##        total = mult(total, num1)
##    return total
##
##def fold(num1, num2, identity, operator):
##    total = identity
##    for i in range(num2):
##        total = operator(total, num1)
##    return total
##
##
##def factorial(num):
##    total = 1
##    for i in range(1, num+1):
##        total = mult(total, i)
##    return total
##        
##
    
    
main()




##factorial_anwser = factorial(5)
##print(factorial_anwser)
##factorial_anwser = factorial(3)
##print(factorial_anwser)
##factorial_anwser = factorial(7)
##print(factorial_anwser)









    
