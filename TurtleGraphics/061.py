import turtle

t = turtle.Pen()
t.turtlesize(3)
t.color('green')
t.shape('turtle')
t.speed(1)
sides = 3
size = 300

t.forward(size)
t.left(90)
t.forward(size)
t.left(135)
t.forward(size + 125)
t.hideturtle()
turtle.exitonclick()

    
