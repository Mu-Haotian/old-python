from arcade import * #导入库

SCREEN_WIDTH = 1000 #长
SCRENN_HEIGHT = 650 #宽
SCREEN_TITLE = "pLATFORMER" #窗口标题

class MyGame(arcade.Window):
    def __init__(self, width , height , title):
        #调用父类并设置窗口
        super().__init__(width , height , title)
        self.setup()
        
    
    def setup(self):
        set_background_color(color.WHITE)

    def on_draw(self):
        start_render()
        self.mydraw()

    def mydraw(self):
        bx,by = 400,300
        draw_rectangle_filled(bx,by + 70 , 100 ,80 ,color.RED)
        draw_rectangle_filled(bx,by + 70 , 40 ,40 ,color.GRAY)
        draw_rectangle_filled(bx,by , 200 , 60 , color.RED)
        draw_circle_filled(bx - 50 , by - 30 , 30 , color.BLACK)
        draw_circle_filled(bx + 50 , by - 30 , 30 , color.BLACK)
        draw_text("--by 木木昊天" , by + 100 , by - 30 - 50 , color.BLUE , font_name= ("simhei","PingFang"))


if __name__ == '__main__':
    game = MyGame(SCREEN_WIDTH,SCRENN_HEIGHT,SCREEN_TITLE)
    run()
