import turtle
t=turtle.Turtle()
t.hideturtle()
list1=["purple","red","orange","blue","green"]
for i in range(200):
    t.color(list1[i%5])
    t.pensize(i/10+1)
    t.forward(i)
    t.left(59)
turtle.done()