# Write a function called power that takes num1 and raises it to the power of num2.
# DON'T USE **. But you may use *, *=, or mult.

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
mult_anwser = fold(3, 3, 0, add)
print(mult_anwser)
power_anwser = fold(3, 3, 1, mult)
print(power_anwser)
















    
