import arcade #导入库

SCREEN_WIDTH = 1000 #长
SCRENN_HEIGHT = 650 #宽
SCREEN_TITLE = "pLATFORMER" #窗口标题

#用于从原始大小缩放精灵的常数
CHARACTER_SCALING = 1
TILE_SCALING = 0.5

class MyGame(arcade.Window):
    def __init__(self):
        #调用父类并设置窗口
        super().__init__(SCREEN_WIDTH,SCRENN_HEIGHT,SCREEN_TITLE)
        arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE)

        self.scene = None

        

        arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE)

    def setup(self):
        #在此处设置游戏。调用此函数可重新启动游戏
        #创建精灵列表
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList(use_spatial_hash=True)

        #设置播放器，特别是将其放置在这些坐标处。
        image_source = ":resources:images/animated_characters/female_adventurer/femaleAdventurer_idle.png"
        self.player_sprite = arcade.Sprite(image_source, CHARACTER_SCALING)
        self.player_sprite.center_x = 64
        self.player_sprite.center_y = 128
        self.player_list.append(self.player_sprite)

        #创造条件
        #这显示了如何使用循环水平放置多个精灵
        for x in range(0, 1250, 64):
            wall = arcade.Sprite(":resources:images/tiles/grassMid.png", TILE_SCALING)
            wall.center_x = x
            wall.center_y = 32
            self.wall_list.append(wall)

        #把一些板条箱放在地上
        #这显示了如何使用坐标列表来放置精灵
            coordinate_list = [[512, 96], [256, 96], [768, 96]]

        for coordinate in coordinate_list:
                #在地上放一个板条箱
            wall = arcade.Sprite(
            ":resources:images/tiles/boxCrate_double.png", TILE_SCALING
        )
            wall.position = coordinate
            self.wall_list.append(wall)
        

    def on_draw(self):
        #渲染屏幕

        self.clear()
        #这里是绘制屏幕的代码

        #画我们的精灵
        self.wall_list.draw()
        self.player_list.draw()


def main():
    #主要功能
    window = MyGame()
    window.setup()
    arcade.run()



if __name__ == "__main__":
    main()

    


