import turtle
import random

colors = ['green','red','black','blue','purple','yellow','#43878a']
randColor = random.choice(colors)

SIZE = random.randint(1,100)
ANGLE = random.randint(-360,360)
NUMBER_OF_LINES = random.randint(1,50)
dirction = random.choice(['right','left'])
t = turtle.Pen()
t.turtlesize(2)
t.shape('turtle')
t.speed(0)
t.color(randColor)

for i in range(NUMBER_OF_LINES):
    NUMBER_OF_LINES = random.randint(1,50)
    ANGLE = random.randint(-360,360)
    SIZE = random.randint(1,100)
    randColor = random.choice(colors)
    t.color(randColor)
    t.left(ANGLE)    
    for i in range(0,NUMBER_OF_LINES):
        t.forward(SIZE)
        t.right(360/NUMBER_OF_LINES)

    
t.hideturtle()
turtle.exitonclick()

