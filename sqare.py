import turtle
t=turtle.Turtle()
t.color("white")
wn=turtle.Screen()
wn.bgcolor("black")
t.speed(1)
t.hideturtle()
t.begin_fill()
t.fillcolor("red")
for i in range(4):
    t.fd(100)
    t.lt(90)
t.end_fill()
turtle.done()