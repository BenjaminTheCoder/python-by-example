import turtle
import random

colors = ['green','red','black','blue','purple','yellow']




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

def mainOrig():
    end = int(input('Enter the end number. '))
    for seq in map(collatz, range(1, end+1)):
        plt.plot(seq)
    plt.show()


EVEN_ANGLE = 10
ODD_ANGLE  = 20
STEP_SIZE  = 5
PEN_SIZE = 2
    
def main():
    end = int(input('Enter the end number. '))
    allSeqs = map(collatz, range(1, end+1))
    turtle.tracer(False)
    for seq in allSeqs:

        
        t = turtle.Pen()
        t.turtlesize(1)
        t.shape('turtle')
        t.width(PEN_SIZE)
        t.speed('fastest')
        t.color(random.choice(colors))
        t.left(90)
        for x in seq:
            if isEven(x):
                t.right(EVEN_ANGLE)
            else:
                t.left(ODD_ANGLE)
            t.forward(STEP_SIZE)
        
        
        t.hideturtle()
    turtle.update()
    turtle.exitonclick()
      
main()

    
    













    
