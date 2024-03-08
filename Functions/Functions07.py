# Write a function called factorial which takes a positive integer and returns the factorial of that integer.

PI = 3.14

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

# anwser = power(3, 3)
##mult_anwser = fold(3, 3, 0, add)
##print(mult_anwser)
##power_anwser = fold(3, 3, 1, mult)
##print(power_anwser)



def factorial(num):
    total = 1
    for i in range(1, num+1):
        total = mult(total, i)
    return total
        
    


factorial_anwser = factorial(5)
print(factorial_anwser)
factorial_anwser = factorial(3)
print(factorial_anwser)
factorial_anwser = factorial(7)
print(factorial_anwser)









    
