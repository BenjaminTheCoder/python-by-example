import turtle

t = turtle.Pen()
t.turtlesize(1)
t.color('green')
t.shape('turtle')
t.speed(1)

for i in range(360):
    t.forward(2)
    t.left(1)
    
t.hideturtle()
turtle.exitonclick()

    
