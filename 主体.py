
import sys;
import pygame;
 
pygame.init();
ck = width,height = 900,800;#长宽
sc = pygame.display.set_mode(ck);#创建窗口
c = (255,255,255);
 
while True:
    for e in pygame.event.get():#获得事件
        if e.type == pygame.QUIT:
            sys.exit();
 
    sc.fill(c);
    pygame.display.flip();
 
pygame.quit();