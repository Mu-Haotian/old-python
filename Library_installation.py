# 导入 alive-progress 库
from alive_progress import alive_bar
import time
import os
import PySimpleGUI as sg

def Plugins():
    layout = [[sg.Text('任务完成进度')],
          [sg.ProgressBar(1000, orientation='h', size=(20, 20), key='progressbar')],
          [sg.Cancel()]]

    # window只需将自定义的布局加载出来即可 第一个参数是窗口标题。
    window = sg.Window('机器人执行进度', layout)

    # 根据key值获取到进度条
    progress_bar = window['progressbar']

    # window的read函数分为同步和异步，
    # 不带timeout参数即为同步函数 一直等到手动点击按钮才会返回。
    # 带timeout参数不为None的为异步函数,timeout时间内无时间或者点击了按钮都会产生结果。
    # 异步方式不会阻塞后面的程序运行。
    for i in range(1000):	# 循环
        event, values = window.read(timeout=10)
        if event == 'Cancel' or event is None:
            break
        progress_bar.UpdateBar(i + 10)

    window.close()
    # 使用 with 语句创建一个进度条
    with alive_bar(4) as bar: # 给 alive_bar 传入进度条总数目（这里是 100）
        for item in range(1):
            name = "pip"
            all = os.popen("pip list").read()

            if name in all:
                print("a")
                bar()
            else:
                os.system(f'python -m pip install --upgrade pip')
                bar()

            name = "urllib"
            all = os.popen("pip list").read()

            if name in all:
                bar()
            else:
                os.system(f'pip install urllib')
                bar()


            name = "json"
            all = os.popen("pip list").read()

            if name in all:
                bar()
            else:
                os.system(f'pip install json')
                bar()
            
            name = "requests"
            all = os.popen("pip list").read()

            if name in all:
                bar()
            else:
                os.system(f'pip install requests')
                bar()
Plugins()            