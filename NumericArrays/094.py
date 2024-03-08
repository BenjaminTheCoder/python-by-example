from array import *


def main():
    nums = array('l',[6, 8, 3])
    print(nums)
    x = int(input('enter one of the following. '))
    while x not in nums:
        x = int(input('enter one of the following!!!!!!!!!!!! '))
    i = nums.index(x)
    print(i)

    
        


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
