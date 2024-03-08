import turtle
import random

colors = ['green','red','black','blue','purple','#43878a']
randColor = random.choice(colors)

NUMBER_OF_LINES = random.randint(1,20)
t = turtle.Pen()
t.turtlesize(2)
t.shape('turtle')
t.speed(0)
t.color(randColor)

for i in range(NUMBER_OF_LINES):
    angle = random.randint(0,360)
    size = random.randint(1,100)
    randColor = random.choice(colors)
    t.color(randColor)
    t.left(angle)    
    t.forward(size)

    
t.hideturtle()
turtle.exitonclick()

