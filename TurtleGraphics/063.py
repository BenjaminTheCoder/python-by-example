import turtle
SPACE = 10
SIZE = 90
t = turtle.Pen()
t.begin_fill()
t.turtlesize(1)
t.color('red')
t.shape('turtle')
t.speed(1)
t.color('black', 'red')
for i in range(4):
    t.forward(SIZE)
    t.left(90)
t.penup()
t.forward(SPACE)
t.end_fill()
t.pendown()
t.color('black', 'white')
t.begin_fill()
for i in range(4):
    t.forward(SIZE)
    t.left(90)
t.penup()
t.forward(SPACE)
t.end_fill()
t.pendown()
t.color('black', 'blue')
t.begin_fill()
for i in range(4):
    t.forward(SIZE)
    t.left(90)

t.end_fill()    
t.hideturtle()
turtle.exitonclick()

    
