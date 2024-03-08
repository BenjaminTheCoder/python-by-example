# Write a function called mult that takes two number args and returns their product.
# DO NOT use the * operator. Use the add function instead of +.

def add(num1, num2):   
    return num1 + num2



def mult(num1, num2):   
    total = 0
    for i in range(num1):
        total = add(total, num2)
    return total
   


anwser = mult(2, 3)
print(anwser)
















    
