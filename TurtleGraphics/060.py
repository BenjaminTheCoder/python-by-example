import turtle

t = turtle.Pen()
t.turtlesize(3)
t.color('green')
##t2 = turtle.Pen()
##t2.shape('turtle')
##t2.right(35)
##t2.forward(200)
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

    
