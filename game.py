from arcade import *
from PIL import *
import random
 
# 设置窗体宽和高
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800

SCREEN_TITLE = "大鱼吃小鱼"

#存储玩家角色每次移动的速度
MOVEMENT_SPEED = 4

LEFT = 0
RIGHT = 1

LEFT_FISH = 0
RIGHT_FISH = 1

luck_umber = random.choice(range(1,20,1))

class Player(Sprite):
    #self表示对象本身，定义__init__函数表示接收实际参数。image是图片路径，角色初始化
    def __init__(self, image):
        super().__init__(image)
        self.center_x = SCREEN_WIDTH // 2
        self.center_y = SCREEN_HEIGHT // 2

        self.append_texture(load_texture(
            "resource/player.png", mirrored=True, scale=1))

        self.size = 2


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
    
    def evolution(self,score):
        if score >= 30:
            self.size = 8
        elif score >= 20:
            self.size = 6
            self.scale = 1.3
        elif score >= 10:
            self.size = 4
            self.scale = 1.2

    def target(self,score):
        if score >= 30:
            self.mb = '红鱼'
        elif score >= 20:
            self.mb = '紫鱼'
            self.scale = 1.3
        elif score >= 10:
            self.mb = '绿鱼'
            self.scale = 1.2
        elif score >= 0:
            self.mb = '黄鱼'  

class Enemy(Sprite):
    def __init__(self, image ):
        super().__init__(image)
        self.Fishs = random.choice(range(1,20,1))
        luck = random.choice(range(1,20,1))
        face = random.choice(["left", "right"])
        speed = random.choice([1,2,3,4,5])
        if luck == luck_umber:
            speed = random.choice([10])

        if face == "left":
            self.center_x = SCREEN_WIDTH + 60
            self.change_x = -speed
        elif face == "right":
            self.center_x = -60
            self.append_texture(load_texture(image,mirrored=True, scale=1))
            self.set_texture(RIGHT)
            self.change_x = speed
        self.center_y = random.randint(0, SCREEN_HEIGHT)

#定义MyGame类 继承arcade.window类


class MyGame(arcade.Window):
    #类初始化
    def __init__(self, width, height,title):
        #super表示调用父类初始化窗体
        super().__init__(width, height,title)

        self.setup()
    #初始化操作都放在setup方法中，并且在init方法中调用，setup是进行游戏的初始化设计 比如游戏的具体数值以及窗体。

    def setup(self):
        #用pillow 调整背景图片大小以适配窗体宽高
        Image.open("resource/sea.png").resize((SCREEN_WIDTH,
                                               SCREEN_HEIGHT )).save("resource/new_sea.png")
        #设置背景图片
        self.background = Sprite("resource/new_sea.png")
        self.background.center_x = SCREEN_WIDTH // 2
        self.background.center_y = SCREEN_HEIGHT // 2
        #添加玩家角色
        self.player_sprite = Player("resource/player.png")
        self.player_sprite_list = SpriteList()
        self.player_sprite_list.append(self.player_sprite)
        self.fishes = {"resource/黄鱼.png":1,
                       "resource/绿鱼.png":3,
                       "resource/红鱼.png":5,
                       "resource/紫鱼.png":7,
                       "resource/蓝鱼.png":9}


        self.enemy_sprite_list = SpriteList()
        self.total_time = 0
        self.last_time = 0
        self.create_num = 1
        self.score = 0
        self.mb = ''


    #绘制的图形需要在这里调用才能在窗体中绘制。
    def on_draw(self):

        #start_render() 表示开始绘制程序之前，先要告诉程序，我们要开始绘制图形了。
        start_render()
        #进行渲染
        self.background.draw()
        #渲染角色图片
        self.enemy_sprite_list.draw()
        self.player_sprite_list.draw()
        self.enemy_sprite_list.update()

        draw_text(f"score:{self.score}",0,SCREEN_HEIGHT - 20,color.WHITE,font_name=("simhei","PingFang"),font_size = 20 )
        draw_text(f"目标:黄鱼",0,SCREEN_HEIGHT - 50,color.WHITE,font_name=("simhei","PingFang"),font_size = 20 )

    def on_update(self, delta_time):     
        #添加更新玩家的代码，调用的20行的update
        self.total_time += delta_time
        if int(self.total_time) != int(self.last_time) and int(self.total_time) %10 == 0:
            self.create_num += 1
        if int(self.total_time) != int(self.last_time) and int(self.total_time) %1 == 0:
            self.create_enemy()
            self.last_time = self.total_time
        self.player_sprite_list.update()
        self.enemy_sprite_list.update()
        for enemy in self.enemy_sprite_list:
            if enemy.center_x < -60 or enemy.center_x  > SCREEN_WIDTH + 60:
                enemy.kill()

        hit_list = check_for_collision_with_list(self.player_sprite,self.enemy_sprite_list)
        if hit_list:
            for hit in hit_list:
                if self.player_sprite.size > hit.size:
                    hit.kill()
                    self.score += 1
                else:
                    self.player_sprite.kill()

        self.player_sprite.evolution(self.score)

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
        for i in range(self.create_num):
            fish = random.choice(list(self.fishes.keys()))
            size = self.fishes[fish]
            enemy_sprite = Enemy(fish)
            enemy_sprite.size = size
            self.enemy_sprite_list.append(enemy_sprite)


if __name__ == '__main__':
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    run()
