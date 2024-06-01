import turtle

t=turtle.Turtle()
s=turtle.Turtle()

t.hideturtle()
t.goto(0,-10)

t.pensize(3)
t.color('red')
t.begin_fill()
t.left(140)
t.forward(180)
t.circle(-90,200)
t.setheading(60)
t.circle(-90,200)
t.forward(178)
t.end_fill()


t.penup()
t.goto(-130,130)
t.pendown()
t.color('white')
t.write("I Love You Miss you", font=("Verdana",19,"bold"))

t.penup()
t.goto(-130,-130)
t.pendown()
t.color('black')
t.write("Agus Susanti", font=("Verdana",25,"bold"))
turtle.done()



