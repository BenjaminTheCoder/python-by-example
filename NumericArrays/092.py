from array import *
from random import randint

def main():
    nums = array('l',[])
    num1 = array('l',[])
    for i in range(5):
        num = randint(1,100)
        num1.append(num)
    for i in range(3):
       num2 = int(input('enter a number. '))
       nums.append(num2)
    nums.extend(num1)
    nums = sorted(nums)
    for x in nums:
        print(x)
        


def getRandomNums(start, end, howMany):
    return array('l', [randint(start, end) for x in range(howMany)])
        
def getUserNums(howMany):
    return array('l', [int(input('Enter a number: ')) for x in range(howMany)])
              
def main2():
    randNums = getRandomNums(1,100,5)
    userNums = getUserNums(3)
    allNums = randNums + userNums
    for x in sorted(allNums):
        print(x)
        
   
    

main2()
