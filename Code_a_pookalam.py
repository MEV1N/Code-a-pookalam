import turtle
screen = turtle.Screen()
screen.title = "Pookalam"
t = turtle.Turtle()
t.speed(0)

t.up()
t.rt(90)
t.fd(250)
t.lt(90)
t.down()

def circle(rad, clr): #function to draw circle and decide its colour

    t.down()
    t.fillcolor(clr)
    t.begin_fill()
    t.circle(rad)
    t.up()
    t.end_fill()

def petal(radius, angle, clr): #function for petals
    t.penup()
    t.goto(0, 0)
    t.setheading(angle)
    t.pendown()
    t.color(clr)
    t.begin_fill()
    t.circle(radius, 90)
    t.left(90)
    t.circle(radius, 90)
    t.end_fill()
def rect(clr): #to draw rectangles
    t.color(clr)
    t.lt(90)
    t.fd(200)
    t.fillcolor(clr)
    t.down()

    for i in range (36):
        t.begin_fill()
        t.circle(100,360,4)
        t.lt(10)
        t.end_fill()
    t.up()

def arc(rad,clr,r):


    t.color(clr)
    t.begin_fill()

    t.fd(rad)
    t.lt(90)
    t.circle(rad, 40)
    t.lt(90)
    t.fd(rad)
    t.rt(4)
    t.end_fill()






circle(250,"dark green") #drawing the first big circle






t.lt(90) #repositioning the turtle
t.fd(10)
t.rt(90)
circle(240,"orange") #2nd circle
t.setposition(x=0, y=0)
r=30
for i in range (5):
    arc(240,"yellow",r)
    r+=20



angle1 = 98
for i in range(5):
    petal(169,angle1,"red")
    angle1+=72

angle2 = 67
for i in range(5):
    petal(169,angle2,"dark green")
    angle2+=72

angle2 = 67
for i in range(5):
    petal(165,angle2,"white")
    angle2+=72

angle2 = 67
for i in range(5):
    petal(115,angle2,"dark green")
    angle2+=72


t.fd(100)
t.lt(90)
circle(100,"dark green")


t.lt(90)
t.fd(2)
t.rt(90)
circle(98,"yellow")


t.lt(90)
t.fd(27)
t.rt(90)
circle(70,"dark green")


t.lt(90)
t.fd(2)
t.rt(90)
circle(68,"orange")


t.lt(90)
t.fd(38)
t.rt(90)
circle(30,"red")


t.lt(90)
t.fd(19)
t.rt(90)
circle(10,"orange")





t.hideturtle()
screen.exitonclick()