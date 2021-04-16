import turtle
t=turtle.Turtle()
t.hideturtle()
t.speed(0)

def draw_circle(x,y,color,rad):
    t.up()
    t.goto(x,y)
    t.down()
    t.begin_fill()
    t.circle(rad)
    t.fillcolor(color)
    t.end_fill()

draw_circle(0,0,"green",50)
draw_circle(200,200,"orange",50)
draw_circle(-200,200,"blue",50)
draw_circle(-200,-200,"red",50)
draw_circle(200,-200,"yellow",25)
draw_circle(200,0,"pink",25)
draw_circle(0,200,"indigo",25)
draw_circle(-200,0,"purple",25)
draw_circle(0,-200,"brown",25)

turtle.done()