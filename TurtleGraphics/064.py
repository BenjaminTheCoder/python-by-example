import turtle
SPACE = 10
SIZE = 50
REAL_SPACE = SPACE + SIZE
t = turtle.Pen()
t.turtlesize(1)
t.color('red')
t.shape('turtle')
t.speed(1)
#for i in range(4):
for i in range(4):
    t.left(35)
    t.forward(100)
    t.left(260)
    t.forward(100)
t.left(35)
t.forward(100)
t.left(260)
t.forward(200)

##t.left(285)
##t.forward(6)
##t.left(235)

t.hideturtle()
turtle.exitonclick()

    
