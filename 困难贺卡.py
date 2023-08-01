# -*- coding: utf-8 -*-
import turtle as T
import random
import time

# 绘图区域
t = T.Turtle()
# 画布大小
w = T.Screen()
t.hideturtle()  # 隐藏画笔
t.getscreen().tracer(5, 0)
w.screensize(bg='maroon')
t.left(90)
t.up()
t.forward(280)
t.down()
t.pensize(3)

# 画五角星
n = 100
t.color("orange", "yellow")
t.begin_fill()
t.left(126)

for i in range(5):
	t.forward(n/5)
	t.right(144)
	t.forward(n/5)
	t.left(71)
t.end_fill()
t.left(60)
t.pensize(8)
t.forward(60)
t.right(20)
t.right(116)
t.pensize(6)

# 画树冠
t.color('dark green')
n = 130

for i in range(6):
	time.sleep(0.5)
	a = 1+i/2
	t.begin_fill()
	t.left(90)
	t.forward(n*a*0.707)
	t.left(135)
	t.forward(n*a)
	t.left(135)
	t.forward(n*a*0.707)
	t.end_fill()
	t.up()
	t.left(90)
	t.forward(n*a*0.707/3)
	t.left(135)
	t.forward(n*a/6)
	t.left(135)
	t.down()

# 画树干
t.up()
t.right(135)
t.forward(30)
t.right(90)
t.forward(157)
t.down()
t.color('saddlebrown')
t.begin_fill()
t.forward(80)
t.right(90)
t.forward(45)
t.right(90)
t.forward(80)
t.right(90)
t.forward(45)
t.end_fill()

t.up()
t.backward(45)
t.right(90)
t.backward(470)
t.down()

# 画灯


def light(l, t):
	t.pensize(3)
	colors = ["magenta", "darkorange", "red", "blue"]
	for i in range(l):
		time.sleep(0.2)
		b = 70+16*i
		a = b/2*random.randint(-100, 100)/100
		t.up()
		t.forward(b)
		t.left(90)
		t.forward(a)
		t.down()
		t.color("lightyellow", colors[i % 4])
		t.begin_fill()
		t.circle(10)
		t.end_fill()
		t.up()
		t.backward(a)
		t.right(90)
		t.backward(b)
		t.down()
	t.pensize(1)

# 画雪花


def snow(m, t):
    for i in range(m):
        a = 400 - 800 * random.random()
        b = 600 - 800 * random.random()
        t.up()
        t.forward(b)
        t.left(90)
        t.forward(a)
        t.down()
        t.color('white')
        t.begin_fill()
        t.circle(1)
        t.end_fill()
        t.up()
        t.backward(a)
        t.right(90)
        t.backward(b)


light(24, t)
snow(600, t)

# 文字
t.goto(-200, 200)
my_word = ("Merry Christmas")
t.write(my_word, font=("Edwardian Script ITC", 40, "bold"))
time.sleep(0.3)
t.goto(-100, 50)
my_word = ("and")
t.write(my_word, font=("Edwardian Script ITC", 50, "bold"))
time.sleep(0.3)
t.goto(-150, -100)
my_word = ("Happy New Year")
t.write(my_word, font=("Edwardian Script ITC", 40, "bold"))

time.sleep()
