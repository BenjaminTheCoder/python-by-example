import turtle
import random

colors = ['green','red','black','blue','purple','#43878a']
randColor = random.choice(colors)

SIZE = 100
NUMBER_OF_SHAPES = 75
NUMBER_OF_SIDES = 8
t = turtle.Pen()
t.turtlesize(2)
t.shape('turtle')
t.speed(0)
t.color(randColor)

for i in range(0,NUMBER_OF_SHAPES):
    randColor = random.choice(colors)
    t.color(randColor)
    t.right(360/NUMBER_OF_SHAPES)    
    for i in range(0,NUMBER_OF_SIDES):
        t.forward(SIZE)
        t.right(360/NUMBER_OF_SIDES)

    
t.hideturtle()
turtle.exitonclick()

