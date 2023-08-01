# -*- coding: utf-8 -*-
from turtle import *
from random import randint


def create_rectangle(turtle, color, x, y, width, height):
    turtle.penup()
    turtle.color(color)
    turtle.fillcolor(color)
    turtle.goto(x, y)
    turtle.pendown()
    turtle.begin_fill()

    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    turtle.left(90)
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    turtle.left(90)

    turtle.end_fill()
    turtle.setheading(0)


def create_circle(turtle, x, y, radius, color):
    oogway.penup()
    oogway.color(color)
    oogway.fillcolor(color)
    oogway.goto(x, y)
    oogway.pendown()
    oogway.begin_fill()
    oogway.circle(radius)
    oogway.end_fill()


BG_COLOR = "#0073e6"
oogway = Turtle()
oogway.hideturtle()
oogway.speed(20)
screen = oogway.getscreen()
screen.bgcolor(BG_COLOR)
screen.title("Merry Christmas")

y = -100
create_rectangle(oogway, "#ff6666", -15, y-60, 30, 60)

width = 240
oogway.speed(0)
while width > 10:
    width = width - 10
    height = 10
    x = 0 - width/2
    create_rectangle(oogway, "green", x, y, width, height)
    y = y + height

oogway.penup()
oogway.color('yellow')
oogway.goto(-20, y+10)
oogway.begin_fill()
oogway.pendown()
for i in range(5):
    oogway.forward(40)
    oogway.right(144)
oogway.end_fill()

tree_height = y + 40

create_circle(oogway, 230, 180, 60, "white")
create_circle(oogway, 220, 180, 60, BG_COLOR)

number_of_stars = randint(20, 30)
for _ in range(0, number_of_stars):
    x_star = randint(-(screen.window_width()//2), screen.window_width()//2)
    y_star = randint(tree_height, screen.window_height()//2)
    size = randint(5, 20)
    oogway.penup()
    oogway.color('white')
    oogway.goto(x_star, y_star)
    oogway.begin_fill()
    oogway.pendown()
    for i in range(5):
        oogway.forward(size)
        oogway.right(144)
    oogway.end_fill()

oogway.penup()
# 祝福语
msg = "圣诞快乐！"
oogway.goto(0, -230)
oogway.color("white")
oogway.pendown()
oogway.write(msg, move=False, align="center", font=("Arial", 22, "bold"))

oogway.hideturtle()
screen.mainloop()
