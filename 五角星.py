import turtle

p = turtle.Turtle()
p.speed(6)
p.pensize(2)
p.color("black","yellow")

q = turtle.Turtle()
q.speed(1)
q.pensize(2)
q.color("black","yellow")

p.begin_fill()
q.begin_fill()
for i in range(5):
    p.forward(200)
    q.forward(-200)
    p.right(144)
    q.left(144)
p.end_fill()
q.end_fill()
