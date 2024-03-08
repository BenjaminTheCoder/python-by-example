import matplotlib.pyplot as plt



def isEven(num):
    return num % 2 == 0

def collatz(x):
    seq = [x]
    while x != 1:
        if isEven(x):
            x  = x // 2
        else:
            x = x * 3 + 1
        seq.append(x)
    return seq

def plotOneSequence():
    x = int(input('Enter a number. '))
    seq = collatz(x)
    plt.plot(seq)
    plt.show()
    
def main():
    end = int(input('Enter the end number. '))
    for seq in map(collatz, range(1, end+1)):
        print(seq)
        plt.plot(seq)
    plt.show()
      


    
#plotOneSequence()    
main()












    
