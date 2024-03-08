from array import *
from random import randint

def main():
    nums = array('l',[])
    for i in range(5):
        num = randint(1,100)
        nums.append(num)
    print(nums)
    for x in nums:
        print(x)
        
   
    

main()
