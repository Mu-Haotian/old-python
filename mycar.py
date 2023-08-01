
from arcade import *

# 设置窗体宽和高
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
# 设置窗体标题
SCREEN_TITLE = "冒险小车"


class Road(Sprite):
    def __init__(self, image):
        super().__init__(image)
        # 车道
        self.center_x = SCREEN_WIDTH//2
        self.center_y = SCREEN_HEIGHT//2
        # 设置车道的改变值
        self.change_y = -3
    # 处理车道逻辑，当车道完全移出窗体，将车道移到窗体的上方

    def update(self):
        super().update()
        if self.center_y <= SCREEN_HEIGHT // 2 - SCREEN_HEIGHT:
            self.center_y = SCREEN_HEIGHT // 2 + SCREEN_HEIGHT


class SmallCar(Sprite):
    def __init__(self,image):
        super().__init__(image)
        self.center_x = SCREEN_WIDTH // 2
        self.center_y = 100

class Cart(Sprite):
    def __init__(self,image):
        super().__init__(image)
        self.center_y = random.randint(
            SCREEN_HEIGHT , SCREEN_HEIGHT + SCREEN_HEIGHT // 2)
        self.change_y = -2
class StatusBar():
    def __init__(self) :
        self.distance = 0
        self.hp = 2

    def draw_bar(self):
        draw_rectangle_filled(
            SCREEN_WIDTH // 2 , SCREEN_HEIGHT - 15 , SCREEN_WIDTH , 30 , color.WHITE)

    def draw_distance(self):
        pos_x = 10
        pos_y = SCREEN_HEIGHT - 20 
        draw_text(f"路程:{self.distance}",pos_x,pos_y,
                    color.BLUE,font_name=("simhei","PingFang"))

    def draw_hp(self):
        pos_x = SCREEN_WIDTH // 2 -50
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
        self.total_time = 0
        self.last_time = 0
        self.status_bar = StatusBar()
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

    def on_update(self, delta_time: float):
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
    #提示
    print("ps:可以用方向键操纵,A,D操纵,4,6操纵")
    def on_key_release(self , symbol: int , modifiers : int):
        #方向键操纵
        #左
        if symbol == key.LEFT and self.small_car.center_x >= SCREEN_WIDTH // 2:
            self.small_car.center_x -= 200
        #右
        if symbol == key.RIGHT and self.small_car.center_x <= SCREEN_WIDTH // 2 :
            self.small_car.center_x += 200
        
        #A,D操纵
        #左
        if symbol == key. A and self.small_car.center_x >= SCREEN_WIDTH // 2:
            self.small_car.center_x -= 200
        #右
        if symbol == key. D  and self.small_car.center_x <= SCREEN_WIDTH // 2 :
            self.small_car.center_x += 200

        #4,6操纵
        #左
        if symbol == key.NUM_4 and self.small_car.center_x >= SCREEN_WIDTH // 2:
            self.small_car.center_x -= 200
        #右
        if symbol == key.NUM_6 and self.small_car.center_x <= SCREEN_WIDTH // 2 :
            self.small_car.center_x += 200


    def create_carts(self):
        cart_list = ("images/大车1.png", "images/大车2.png", "images/大车3.png")

        num = 2
        x = random.sample(
            [SCREEN_WIDTH // 2 - 200 , SCREEN_WIDTH // 2 , SCREEN_WIDTH // 2 + 200] , 2)
        for i in range(num):
            cart = Cart(random.choice(cart_list))
            cart.center_x = x[i]
            self.carts.append(cart)
    

if __name__ == '__main__':
    game = MyCar(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    run()
