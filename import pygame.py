import pygame 
import sys
import os
'''常量'''
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
SCREEN_TITLE = "标题"
'''常量'''

def initialize_pygaem():
    #初始化pygame
    pygame.init()
    #检测初始化
    initialize = pygame.get_init()
    #初始化成功
    if initialize == True:
        print("初始化成功")
    #初始化失败
    if initialize == False:
        print("初始化失败")

    #获取 SDL 的版本号
    SDL = pygame.get_sdl_version()
    print("SDL的版本号是:" + str(SDL))
    version = pygame.version.ver

    #检测设备
    Inspection_equipment = os.name

    if pygame.version.vernum < (2,1,1):
        print("您的pygame版本过低,请更新pygame,如果要更新pygame请输入Y,如果不更新就输入N")
        update = input("请输入Y/n")
        if update == "Y" or "y":
            print("正在更新pip")
            package_name = 'pip'
            os.system(f'pip install {package_name}')

            print("")
            print("正在下载pygame")
            package_name = 'pygame'
            os.system(f'pip install {package_name}')

            print("")
            print("正在查验是否安装成功pygame")
            package_name = 'pygame'
            os.system(f'pip install {package_name}')
            os.system(f'pip install {package_name}')
            os.system(f'pip install {package_name}')

            print("")
            print("成功安装pygame")
            print("")
            print("尽情的玩游戏吧")

        if update == "n" or "N": 
            print("如果不更新pygame会导致一些功能不可用")

#初始化
initialize_pygaem()
#创建game父类
class game():
    def __init__(self) :
        pass

if __name__ == "__main__":
    #创建窗口
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    #创建窗口标题
    pygame.display.set_caption(SCREEN_TITLE)

    #无限循环让窗口一直保持出现
    while True:
        for event in pygame.event.get():
            #检测事件
            if event.type == pygame.QUIT:
                print("")
                #获取后台
                background = pygame.display.Info()
                print(background)

                print("正在退出程序")
                #删除Pygaem模块
                print("正在删除Pygaem模块")
                pygame.quit()

                #退出程序
                print("退出成功!")
                sys.exit()



