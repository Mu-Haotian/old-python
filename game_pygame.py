import time
import sys
import random
import math
import os
import getopt
import pygame
from socket import *
from pygame.locals import *

#常量
WIDTH = 1500  # 游戏窗口的宽度
HEIGHT = 800 # 游戏窗口的高度
TITLE = "大鱼吃小鱼" #游戏窗口的标题
FPS = 60 # 帧率

# RGB模式 (R, G, B)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
CADETBLUE1 = (52,245,255)

class Demo(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()   # 调用父类初始化方法
        self.image = pygame.image.load(r"C:\Users\Administrator\Desktop\fish\resource\player.png")   # pygame.image.load 方法加载图像 
        self.rect =  self.image.get_rect()   # get_rect() 方法获取图像矩形区域
    
    def pygame_test():
        #初始化工作
        print("初始化中…………")
        pygame.init()
        pygame.font.init()
        print("初始化成功") 
        #创建窗体
        game_window = pygame.display.set_mode((WIDTH , HEIGHT))
        pygame.display.set_caption(TITLE)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            # 填充游戏窗口颜色
            game_window.fill(CADETBLUE1)
            # 重新绘制游戏窗口，使其可见
            pygame.display.flip()

    def update(self):   # 图像的更新
        demo = Demo("player")   # 创建精灵
        demo_Group = pygame.sprite.Group()   # 创建精灵组
        demo_Group.add(demo)   # 将精灵添加进精灵组      

        demo_Group.update()   # 让精灵组中的所有精灵调用各自的 update() 方法
        demo_Group.draw(Demo)   # 将精灵绘制在屏幕
    
    def __init__(self):
        game.pygame_test()

    


if __name__ == '__main__': 
    game = Demo()
    game.pygame_test()

