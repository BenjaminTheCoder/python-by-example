# Modify your program to be a function called collatz that takes a number and returns the collatz sequence as a list of numbers.
# In main, ask the user to enter a positive integer. Pass this integer to the collatz function and store the resulting sequence (list) in a variable.
# Print the sequence.
# Tip: use the .append() method on the list of numbers to add new numbers to the list.


def isEven(num):
    return num % 2 == 0

def collatz(x):
    seq = [x]
    while x != 1:
        if isEven(x):
            x  = x // 2
        else:
            x = x * 3 + 1
        seq.append(x)
    return seq

def main():
    x = int(input('Enter a number. '))
    seq = collatz(x)
    print(seq)

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









    
