from tkinter import *

print('Times Tables 1-10')

def part1(num):
    intiger = num
    for i in range(1, 11):
        ans = intiger * i
        print(f'{num} * {i} = {ans}')
        
def part2():
    for i in range(1, 11):
        part1(i)

def main():
    for i in range(1, 11):
        for j in range(1, 11):
            print(f'{i} * {j} = {i*j}')

# part2()
main()