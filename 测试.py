import pygame
#引入pygame中所有常量，比如 QUIT
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((500,250))
pygame.display.set_caption('c语言中文网')
#加载一张图片
image_surface = pygame.image.load("C:\Users\Administrator\Desktop\fish\resource\sea.png").convert()
# rect(left,top,width,height)指定图片上某个区域
# special_flags功能标志位,指定颜色混合模式，默认为 0 表示用纯色填充
image_surface.fill((0,0,255),rect=(100,100,100,50),special_flags=0)
# 200,100 表示图像在水平、垂直方向上的偏移量，以左上角为坐标原点
image_surface.scroll(100,50)
# 无限循环，让窗口停留
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
    # 将图像放置在主屏幕上
    screen.blit(image_surface,(0,0))
    pygame.display.update()
