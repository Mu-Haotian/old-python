from arcade import *
from PIL import Image
import random

# 设置窗体宽和高
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 600

SCREEN_TITLE = "大鱼吃小鱼"

#存储玩家角色每次移动的速度
MOVEMENT_SPEED = 4

LEFT = 0
RIGHT = 1


class Player(Sprite):
    #self表示对象本身，定义__init__函数表示接收实际参数。image是图片路径，角色初始化
    def __init__(self, image):
        super().__init__(image)
        self.center_x = SCREEN_WIDTH // 2
        self.center_y = SCREEN_HEIGHT // 2

        self.append_texture(load_texture(
            "resource/player.png", mirrored=True, scale=1))

    def update(self):
        super().update()
        if self.left < 0:
            self.left = 0
            #如果图片的右边缘大与窗体右边缘也就是窗体的宽度
        elif self.right > SCREEN_WIDTH:
            self.right = SCREEN_WIDTH
          #同样的图片的上边是否大与窗体上边缘，也就是窗体高度
        if self.top > SCREEN_HEIGHT:
            self.top = SCREEN_HEIGHT
            #图片的下边是否小于窗体下边缘，也就是0
        elif self.bottom < 0:
            self.bottom = 0


class Enemy(Sprite):
    def __init__(self, image):
        super().__init__(image)


#定义MyGame类 继承arcade.window类
class MyGame(arcade.Window):
    #类初始化
    def __init__(self, width, height, title):
        #super表示调用父类初始化窗体
        super().__init__(width, height, title)
        #窗口初始化
        self.setup()
    #初始化操作都放在setup方法中，并且在init方法中调用，setup是进行游戏的初始化设计 比如游戏的具体数值以及窗体。

    def setup(self):
        #用pillow 调整背景图片大小以适配窗体宽高
        Image.open("resource/sea.png").resize((SCREEN_WIDTH,
                                               SCREEN_HEIGHT)).save("resource/new_sea.png")
        #设置背景图片
        self.background = Sprite("resource/new_sea.png")
        self.background.center_x = SCREEN_WIDTH // 2
        self.background.center_y = SCREEN_HEIGHT // 2
        #添加玩家角色
        self.player_sprite = Player("resource/player.png")

        self.fishes = ["resouce/黄鱼.png",
                       "resouce/绿鱼.png",
                       "resouce/红鱼.png",
                       "resouce/紫鱼.png",
                       "resouce/蓝鱼.png"]

        self.enemy_sprite_list = SpriteList()

        for i in range(5):
            self.create_enemy()

    #绘制的图形需要在这里调用才能在窗体中绘制。
    def on_draw(self):
        #start_render() 表示开始绘制程序之前，先要告诉程序，我们要开始绘制图形了。
        start_render()
        #进行渲染
        self.background.draw()
        #渲染角色图片
        self.enemy_sprite_list.draw()

    def on_update(self, delta_time):
        #添加更新玩家的代码，调用的20行的update
        self.player_sprite.update()

    #固定的参数。self，symbol，modifiers。
    def on_key_press(self, symbol, modifiers):  # 按下某个键时触发
        #判断是否按下键盘上方向键，也就是up。如果按下，就给角色一个向上的速度MOVEMENT_SPEED，并且赋值给player_sprite.change_y。
        if symbol == key.UP:
            self.player_sprite.change_y = MOVEMENT_SPEED
     #判断是否按下键盘下方向键，也就是down。如果按下，就给角色一个向下的速度MOVEMENT_SPEED（向下为负值），并且赋值给player_sprite.change_y。
        elif symbol == key.DOWN:
            self.player_sprite.change_y = -MOVEMENT_SPEED
      #判断是否按下键盘左方向键，也就是left。如果按下，就给角色一个向左的速度MOVEMENT_SPEED（向左为负值），并且赋值给player_sprite.change_x。
        elif symbol == key.LEFT:
            self.player_sprite.change_x = -MOVEMENT_SPEED
            self.player_sprite.set_texture(LEFT)
      #判断是否按下键盘右方向键，也就是right。如果按下，就给角色一个向右的速度MOVEMENT_SPEED，并且赋值给player_sprite.change_x。
        elif symbol == key.RIGHT:
            self.player_sprite.change_x = MOVEMENT_SPEED
            self.player_sprite.set_texture(RIGHT)
        elif symbol == key.RETURN:
            image = get_image(0, 0, SCREEN_WIDTH*2, SCREEN_HEIGHT*2)
            image.save("screenshot.png")

    def on_key_release(self, symbol, modifiers):  # 松开某个键时触发松开后，把change_x或者y变为0，否则就一直移动。
        #判断方向键上下是否松开，如果松开把速度变为0，也就是不再上下移动。
        if symbol == key.UP or symbol == key.DOWN:
            self.player_sprite.change_y = 0
        #判断方向键左右是否松开，如果松开把速度变为0，也就是不再左右移动。
        elif symbol == key.LEFT or symbol == key.RIGHT:
            self.player_sprite.change_x = 0

    def create_enemy(self):
        fish = random.choice(self.fishes)
        enemy_sprite = Enemy(fish)
        self.enemy_sprite_list.append(enemy_sprite)


if __name__ == '__main__':
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    run()
