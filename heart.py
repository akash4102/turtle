import turtle
t=turtle.Turtle()
t.hideturtle()
t.begin_fill()
t.fillcolor("red")
t.left(40)
t.circle(300,extent=40)
t.right(20)
t.circle(80,extent=180)
t.right(120)
t.circle(80,extent=180)
t.right(20)
t.circle(300,extent=50)
# t.up()
# t.goto(0,0)
# t.down()
# t.right(120)
# t.circle(200,extent=13)
t.end_fill()
turtle.done()