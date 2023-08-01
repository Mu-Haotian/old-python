from multiprocessing import Process
import time
import os
from tkinter import Pack


package_name = 'arcade'

def processes1(intervel):
    print("子进程(%s)开始执行,它的父进程是(%s)" %(os.getpid() ,os.getppid()) )        #获取父进程数据
    #sleep()函数 = 休眠时间
    time.sleep(intervel)      #intervel = 休眠时间 注:要导入time库
    #以下是子进程运行代码
    print("开始运行子进程") 
    os.system(f'pip install {package_name}')

def processes2(intervel):
    print("子进程(%s)开始执行,它的父进程是(%s)" %(os.getpid() ,os.getppid()) )        #获取父进程数据
    #sleep()函数 = 休眠时间
    time.sleep(intervel)      #intervel = 休眠时间 注:要导入time库
    os.system(f'pip install {package_name}')

def processes3(intervel):
    print("子进程(%s)开始执行,它的父进程是(%s)" %(os.getpid() ,os.getppid()) )        #获取父进程数据
    #sleep()函数 = 休眠时间
    time.sleep(intervel)      #intervel = 休眠时间 注:要导入time库
    os.system(f'pip install {package_name}')

def main(): #主进程函数
    print("主进程开始")
    print('主进程的PID:%s' % os.getpid()) #打印主进程的PID
    
    

    Child_processes1 = Process(target=processes1,  #主进程运行processes1()
                               name="Child_processes1",   #Child_processes1进程的名字
                               args=(0,))    #返回数据

    Child_processes2 = Process(target=processes2,  #主进程运行processes2()
                               name="Child_processes2",   #Child_processes2进程的名字
                               args=(0,))    #返回数据

    Child_processes3 = Process(target=processes3,  #主进程运行processes2()
                               name="Child_processes2",   #Child_processes2进程的名字
                               args=(0,))    #返回数据


    Child_processes1.start()   #用start()运行Child_processes1
    Child_processes2.start()   #用start()运行Child_processes2
    Child_processes3.start()   #用start()运行Child_processes3

    print('Child_processes1.ls_alive=%s' % Child_processes1.is_alive())   #判断Child_processes1当前状态
    print('Child_processes1.name=%s' % Child_processes1.name)
    print('Child_processes1.id=%s' % Child_processes1.pid)

    print('Child_processes2.ls_alive=%s' % Child_processes2.is_alive())   #判断Child_processes2当前状态
    print('Child_processes2.name=%s' % Child_processes2.name)
    print('Child_processes2.id=%s' % Child_processes2.pid)

    print('Child_processes3.ls_alive=%s' % Child_processes3.is_alive())   #判断Child_processes3当前状态
    print('Child_processes3.name=%s' % Child_processes3.name)
    print('Child_processes3.id=%s' % Child_processes3.pid)

    Child_processes1.join()
    Child_processes2.join()
    Child_processes3.join()

    print('主进程结束')

if __name__ == '__main__':
    main()
 
