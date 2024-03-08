


def main():
    nums = [[2, 5, 8],[3, 7, 4],[1, 6, 9],[4, 2, 0]]
    row = int(input('enter a row '))
    print(nums[row])
    column = int(input('enter a column in this row '))
    print(nums[row][column])
    change = input('would you like to change this number? ')
    if change == 'y':
        num = int(input('what number? '))
        nums[row][column] = num
    print(nums[row])

        
    


main()        










































