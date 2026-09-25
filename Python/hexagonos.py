import turtle
from turtle import *
from random import randint
 
setup(800, 800)
Screen()
turtle = turtle.Turtle()
turtle.speed(0)
showturtle()
parar = False
 
def avanzar(long):     
    turtle.forward(long)
 
def up(long):
    turtle.setheading(90)    
    avanzar(long)
 
def down(long):
    turtle.setheading(270)
    avanzar(long)
 
def left(long):
    turtle.setheading(180)
    avanzar(long) 
 
def right(long):
    turtle.setheading(0)
    avanzar(long)

def upleft(long):
    turtle.setheading(120)
    avanzar(long)

def upright(long):
    turtle.setheading(60)
    avanzar(long)

def downleft(long):
    turtle.setheading(240)
    avanzar(long)

def downright(long):
    turtle.setheading(300)
    avanzar(long)

def hexagono(long):
    turtle.fillcolor('red')
    turtle.begin_fill()    
    for i in range(6):
        turtle.forward(long)
        turtle.right(60)
    turtle.end_fill()
 
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

#listen()
#onkey(lambda: up(10), 'Up')
#onkey(lambda: down(10), 'Down')
#onkey(lambda: left(10), 'Left')
#onkey(lambda: right(10), 'Right')
#onkey(irRandom, 'R')
#onkey(stop, 'P')
#onkey(clear, 'C')    

turtle.penup()
up(400)
left(385)
turtle.pendown()

totalwidth = 12;
height = 20;
for j in range (height):
    turtle.pendown()
    turtle.setheading(0)
    if j % 2 == 0:
        width = totalwidth        
    else:
        width = totalwidth - 1
    for i in range(width):
        hexagono(25)
        turtle.penup()
        right(75)
        turtle.pendown()
    turtle.penup()
    totalleft = (totalwidth - 1) * 75 + 25 * 1.5
    left(totalleft)
    down(21)

mainloop()
