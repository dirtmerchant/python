#!/usr/bin/env python3

import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")
wn.title("Clock")

dict = {}
x = 30

for turtleName in ["one","two","three","four","five","six","seven","eight","nine","ten","eleven","twelve"]:
    dict[turtleName] = turtle.Turtle()
    dict[turtleName].color("blue")
    dict[turtleName].hideturtle()

for turtleName in ["three","six","nine","twelve"]:
    dict[turtleName].shape("turtle")

for turtleName in ["four","five","six","seven","eight","nine","ten","eleven","twelve","one","two"]:
    dict[turtleName].right(x)
    x = x + 30

for turtleName in ["one","two","three","four","five","six","seven","eight","nine","ten","eleven","twelve"]:
    dict[turtleName].penup()
    dict[turtleName].forward(160)
    dict[turtleName].pendown()
    dict[turtleName].forward(30)
    dict[turtleName].penup()
    dict[turtleName].forward(30)
    dict[turtleName].pendown()
    dict[turtleName].showturtle()

wn.mainloop()
