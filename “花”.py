import turtle




def draw_diamond(turt):

    for i in range(1, 3):

        turt.forward(100)  # 向前走100步

        turt.right(45)  # 然后海龟头向右转45度

        turt.forward(100)  # 继续向前走100步

        turt.right(135)  # 然后有向右转135度


def draw_art():


    window = turtle.Screen()

    window.bgcolor("blue")


    brad = turtle.Turtle()  # 创建一个Turtle的实例

    brad.shape("turtle")  # 形状是一个海龟除了画海龟还可以画箭头，圆圈等等

    brad.color("orange")  # 颜色是橙色

    brad.speed('fast')  # 画的速度是快速


    for i in range(1, 10000):  # 循环36次

        draw_diamond(brad)  # 单画一个菱形也就是花瓣

        brad.right(10)  # 旋转10度

        brad.right(90)  # 当花全部花完一周后，把海龟的头向右转90度

        brad.forward(300)  # 花一根长的线


    window.exitonclick()

draw_art()  # 调用函数
