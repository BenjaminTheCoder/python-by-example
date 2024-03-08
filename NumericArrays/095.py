from array import *


def main():
    nums = array('d',[10.65, 67.55, 46.47, 57.24, 65.54])
    print(nums)
    x = float(input('enter a divser. '))
    for d in nums:
        print(round(d / x, 2))
    

    
        


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
