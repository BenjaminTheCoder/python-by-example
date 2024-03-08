from array import *


def main():
    nums = array('l',[])
    for i in range(5):
       num = int(input('enter a number. '))
       nums.append(num)
       
    nums = sorted(nums)
    print(nums)
    x = int(input('Which number would you like to remove. '))
    nums.remove(x)
    print(nums)
    
        


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
        
   
    

main()
