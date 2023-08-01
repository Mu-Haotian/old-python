'''
---------------UTF-8----------------
Title of the work : mycar
type : Racing games
pip : arcade == 2.0.9
'''
'''
函数介绍:
Road(Sprite) #车道主体函数
SmallCar(Sprite) #白条主体函数
Cart(Sprite) #车图标主体函数
StatusBar() #血量和路程主体函数
MyCar(arcade.Window) #绘制小车
on_update(self, delta_time: float) #移动侦测
'''

import threading
import time
from arcade import *

'''常量请勿修改'''
# 设置窗体宽和高
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
# 设置窗体标题
SCREEN_TITLE = "冒险小车"


class Road(Sprite):
    def __init__(self, image):
        super().__init__(image)
        # 车道
        self.center_x = SCREEN_WIDTH // 3
        self.center_y = SCREEN_HEIGHT // 2
        # 设置车道的改变值
        self.change_y = -3
    # 处理车道逻辑，当车道完全移出窗体，将车道移到窗体的上方

    def update(self):
        super().update()
        if self.center_y <= SCREEN_HEIGHT // 2  - SCREEN_HEIGHT:
            self.center_y = SCREEN_HEIGHT // 2  + SCREEN_HEIGHT


class SmallCar(Sprite):
    def __init__(self,image):
        super().__init__(image)
        self.center_x = SCREEN_WIDTH // 3
        self.center_y = 100

class Cart(Sprite):
    def __init__(self,image):
        super().__init__(image)
        self.center_y = random.randint(
            SCREEN_HEIGHT , SCREEN_HEIGHT + SCREEN_HEIGHT // 3)
        self.change_y = -2

class GameOver(Sprite):
    def __init__(self,image):
        super().__init__(image)
        self.center_x = SCREEN_WIDTH // 3
        self.center_y = SCREEN_HEIGHT // 3

class StatusBar():
    def __init__(self) :
        self.distance = 0
        self.hp = 2
        self.psf = 0
        self.Oil = 10
        self.calculator = 0

    def draw_bar(self):
        draw_rectangle_filled(
            SCREEN_WIDTH // 0.9 - 33 , SCREEN_HEIGHT - 400 , SCREEN_WIDTH , 1000 , color.WHITE)

    def draw_distance(self):
        pos_x = + 700
        pos_y = SCREEN_HEIGHT - 20 
        draw_text(f"路程:{self.distance}",pos_x,pos_y,
                    color.BLUE,font_name=("simhei","PingFang"))

    def draw_hp(self):
        pos_x = SCREEN_WIDTH -100
        pos_y = SCREEN_HEIGHT - 20 
        draw_text(f"血量:",pos_x,pos_y,color.BLUE,
                    font_name=("simhei","PingFang"))
        hearts = SpriteList()        
        for i in range(self.hp):
            heart = Sprite("images/血量.png")
            heart.center_x = pos_x + 50 + heart.width * i
            heart.center_y = pos_y + 5
            hearts.append(heart)
        hearts.draw()

    def Frame_rate(self):
        pos_x = + 900
        pos_y = SCREEN_HEIGHT - 20 
        draw_text(f"FPS:{self.psf}",pos_x,pos_y,
                    color.BLUE,font_name=("simhei","PingFang"))

    def Oil_volume(self):
        pos_x = SCREEN_WIDTH -500
        pos_y = SCREEN_HEIGHT -60
        draw_text(f"油量:",pos_x,pos_y,color.BLUE,
                    font_name=("simhei","PingFang"))
        hearts = SpriteList() 
        for i in range(self.Oil):
            heart = Sprite("images/油量.png")
            heart.center_x = pos_x + 50 + heart.width * i
            heart.center_y = pos_y + 5
            hearts.append(heart)
            self
        hearts.draw()



class MyCar(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        # 窗口初始化
        self.setup()

    def setup(self):
        self.road1 = Road("images/车道.png")
        self.road2 = Road("images/车道.png")
        self.road2.center_y = SCREEN_HEIGHT // 2 + SCREEN_HEIGHT
        # 小车
        self.small_car = SmallCar("images/小车1.png")
        self.carts = SpriteList()
        self.create_carts()
        self.psf_compute = 0
        self.total_time = 0
        self.last_time = 0
        self.status_bar = StatusBar()
        self.game_status = True
        self.gameover = GameOver("images/gameover.png")

    def on_draw(self):
        start_render()
        # 绘制车道
        self.road1.draw()
        self.road2.draw()
        # 绘制小车
        self.small_car.draw()
        for cart in self.carts:
            cart.draw()
        self.status_bar.draw_bar()
        self.status_bar.draw_distance()
        self.status_bar.draw_hp()
        self.status_bar.Frame_rate()
        self.status_bar.Oil_volume()
        if not self.game_status:
            self.gameover.draw()


    def on_update(self, delta_time: float):
        if self.game_status:
            # 移动小车
            self.small_car.update()
            # 移动车道
            self.road1.update()
            self.road2.update()
            for cart in self.carts:
                cart.update()
                if cart.top < 0 :
                    cart.kill()
            self.total_time += delta_time
            if int(self.last_time)  != int(self.total_time) and int(self.total_time)  % 6 == 0:
                self.create_carts()
                self.last_time = self.total_time
            self.status_bar.distance = int(self.total_time)
            self.status_bar.calculator = int(self.total_time)
            self.psf_compute = 1 / delta_time
            self.status_bar.psf = int(self.psf_compute)
            hit_list = check_for_collision_with_list(self.small_car , self .carts)
            if hit_list:
                for hit in hit_list:
                    hit.kill()
                    self.status_bar.hp -= 1
            self.judge_game_status()
        
        #提示
    print("ps:可以用方向键操纵,A,D操纵,4,6操纵")
    def on_key_release(self , symbol: int , modifiers : int):
        if self.game_status:
            #方向键操纵
            #左
            if symbol == key.LEFT and self.small_car.center_x >= SCREEN_WIDTH // 3:
                self.small_car.center_x -= 200
            #右
            if symbol == key.RIGHT and self.small_car.center_x <= SCREEN_WIDTH // 3:
                self.small_car.center_x += 200
            
            #A,D操纵
            #左
            if symbol == key. A and self.small_car.center_x >= SCREEN_WIDTH // 3:
                self.small_car.center_x -= 200
            #右
            if symbol == key. D  and self.small_car.center_x <= SCREEN_WIDTH // 3:
                self.small_car.center_x += 200

            #4,6操纵
            #左
            if symbol == key.NUM_4 and self.small_car.center_x >= SCREEN_WIDTH // 3:
                self.small_car.center_x -= 200
            #右
            if symbol == key.NUM_6 and self.small_car.center_x <= SCREEN_WIDTH // 3 :
                self.small_car.center_x += 200


    def create_carts(self):
        cart_list = ("images/大车1.png", "images/大车2.png", "images/大车3.png")

        num = 2
        x = random.sample(
            [SCREEN_WIDTH // 3 - 200 , SCREEN_WIDTH // 3 , SCREEN_WIDTH // 3 + 200] , 2)
        for i in range(num):
            cart = Cart(random.choice(cart_list))
            cart.center_x = x[i]
            self.carts.append(cart)
    
    def judge_game_status(self):
        if self.status_bar.hp <= 0:
            self.game_status = False

if __name__ == '__main__':
    game = MyCar(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    run()
