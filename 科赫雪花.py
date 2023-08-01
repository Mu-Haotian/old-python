import turtle


#分形雪花
t = turtle.Pen()

def snow(size, n):
    if (n == 0) :
        t.forward(size)
    else :
        for angel in [0,60,(-120),60]:
            t.left(angel)
            #函数调用自身，这种调用方式叫做递归
            #递归时参数变小，画的是更小的雪花
            snow(size / 3, n - 1)

def draw():
    t.speed(0)
    t.penup()
    t.goto((-200), 100)
    t.pendown()
    t.pensize(2)
    level = 3
    snow(400, level)
    t.right(120)
    snow(400, level)
    t.right(120)
    snow(400, level)
    turtle.done()

#开始进入Python的世界
draw()
