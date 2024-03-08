from array import *

def main():
    nums = array('l',[]) 
    while len(nums) != 5:
        num = int(input('Enter a number. '))
        # if num >= 10 and num <= 20:
        if 10 <= num <= 20:    
            nums.append(num)
        else:
            print('NUMBER OUT SIDE OF RANGE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
    print('THANK YOU!!!!!!!!!!!!!')
    for x in nums:
        print(x)
        
              

        
   
    

main()
