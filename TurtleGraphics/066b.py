import turtle
import random

colors = ['green','red','black','blue','purple','yellow']
randColor = random.choice(colors)

SIZE = 50
ANGLE = 72
t = turtle.Pen()
t.turtlesize(1)
t.shape('turtle')
t.speed(1)

for i in range(0,8):
    randColor = random.choice(colors)
    t.color(randColor)
    t.forward(100)
    t.right(45)

    
t.hideturtle()
turtle.exitonclick()

