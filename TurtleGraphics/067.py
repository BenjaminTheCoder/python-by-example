import turtle
import random

colors = ['green','red','black','blue','purple','yellow']
randColor = random.choice(colors)

SIZE = 50
ANGLE = 72
t = turtle.Pen()
t.turtlesize(1)
t.shape('turtle')
t.speed(0)

for i in range(0,10):
    t.right(36)
    for i in range(0,8):
        t.forward(100)
        t.right(45)

    
t.hideturtle()
turtle.exitonclick()

