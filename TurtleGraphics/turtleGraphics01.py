import turtle

t = turtle.Pen()
t.speed(1)
sides = 10
size = 100
for i in range(sides):
    t.forward(size)
    t.left((360/sides))

