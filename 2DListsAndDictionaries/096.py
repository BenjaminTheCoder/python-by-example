


def main():
    print([[2, 5, 8], [3, 7, 4], [1, 6, 9], [4, 2, 0]])
    
        


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
