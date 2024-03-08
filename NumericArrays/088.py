from array import *

def main():
    nums = array('l',[])
    for i in range(5):
        num = int(input('enter a number. '))
        nums.append(num)
    nums = sorted(nums)
    nums.reverse()
    print(nums)
        
   
    

main()
