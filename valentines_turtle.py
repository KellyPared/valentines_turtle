import turtle
import random
v = turtle.Turtle()
v.speed(0)

z = 2
colors  = ["pink","deep pink", "medium violet red", "dark red", "magenta", "red", "linen" ]

def heart(x,y,z,clr):
    v.penup()
    v.goto(x,y)
    v.pendown()
    v.begin_fill()
    v.color(clr)
    v.pensize(5)
    v.pencolor("black")
    for i in range(4):
        v.forward(100/z)
        v.right(90)
    v.end_fill()
    v.goto(x,y)
    v.pencolor("red")
    v.begin_fill()
    v.color(clr)
    v.circle(-(50/z))
    v.right(90)
    v.circle(50/z)
    v.end_fill()

def write(x,y):
    v.penup()
    v.goto(x,y)
    v.backward(x + 200)
    v.right(x)
    v.pendown()
    v.write("Happy Valentines Day\n Will you be my Valentine?" , font = "arial, 20")
    
v.penup()
v.goto(-300,300)

v.pendown()


for i in range(4):
    v.pensize(7)
    v.pencolor("black")
    v.forward(600)
    v.right(90)

for i in range(25):
    clr = random.choice(colors)
    x = random.randint(-200, 200)
    y = random.randint(-200, 200)
    write(x, y)
    x +=10
    y += 10
    heart(x,y,z,clr)
    

            







