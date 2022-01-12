# Simple Pong Game with Python

import turtle

#Create window
wnd = turtle.Screen()
wnd.title("Pong by @1Les_Ter")
wnd.bgcolor("black")
wnd.setup(width=800, height=600)
wnd.tracer(0)


#Main Game Loop
while True:
    wnd.update()