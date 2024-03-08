import turtle

SIZE = 50
t = turtle.Pen()
t.turtlesize(1)
t.color('red')
t.shape('turtle')
t.speed(1)

# 1
t.left(90)
t.forward(SIZE +50)
t.right(90)
t.penup()
t.forward(SIZE)
t.pendown()

# 2
t.forward(SIZE)
t.right(90)
t.forward(SIZE)
t.right(90)
t.forward(SIZE)
t.left(90)
t.forward(SIZE)
t.left(90)
t.forward(SIZE)
t.penup()
t.forward(SIZE)
t.pendown()

# 3
t.forward(SIZE)
t.left(90)
t.forward(SIZE)
t.left(90)
t.forward(25)
t.right(180)
t.forward(25)
t.left(90)
t.forward(SIZE)
t.left(90)
t.forward(SIZE)

t.hideturtle()
turtle.exitonclick()
  
