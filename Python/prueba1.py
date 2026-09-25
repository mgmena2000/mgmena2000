import turtle
from turtle import *
from random import randint
 
setup(800, 800)
Screen()
turtle = turtle.Turtle()
turtle.speed(0)
showturtle()
parar = False
 
 
def up():
    turtle.setheading(90)
    turtle.forward(10)
 
 
def down():
    turtle.setheading(270)
    turtle.forward(10)
 
 
def left():
    turtle.setheading(180)
    turtle.forward(10)
 
 
def right():
    turtle.setheading(0)
    turtle.forward(10)
 
def irRandom():
    while parar == False:    
        steps = randint(1, 5)
        angle = randint(1, 360)
        r = randint(0, 100) / 100
        g = randint(0, 100) / 100
        b = randint(0, 100) / 100
        turtle.pencolor(r, g, b)
        turtle.right(angle)
        turtle.fd(steps)

def stop():
    parar = True

def clear():
    turtle.clear()
    turtle.reset()

listen()
onkey(up, 'Up')
onkey(down, 'Down')
onkey(left, 'Left')
onkey(right, 'Right')
onkey(irRandom, 'R')
onkey(stop, 'P')
onkey(clear, 'C')
 
mainloop()
