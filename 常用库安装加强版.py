import platform
import sys
import os
import traceback
import turtle
import time

common_version = {
    'pyecharts': ['pyecharts==0.5.10', 'pyecharts-snapshot==0.1.8'],
    'pyecharts-snapshot': ['pyecharts==0.5.10', 'pyecharts-snapshot==0.1.8'],
    'pillow': ['pillow==6.1.0'],
    'matplotlib': ['matplotlib==3.1.2'],
    'pyside2': ['PySide2==5.12.3'],
    'arcade': ['arcade==2.0.9'],
    'dataclasses': ['dataclasses==0.7'],
    'snownlp': ['snownlp==0.12.3'],
    'nltk': ['nltk==3.4.5'],
    'echarts-countries-pypkg': ['echarts-countries-pypkg==0.1.6'],
    'jieba': ['jieba==0.39'],
    'reportlab': ['reportlab==3.5.23'],
    'wordcloud': ['wordcloud==1.5.0'],
    'imageio': ['imageio==2.5.0'],
    'pygame': ['pygame==1.9.6'],
    'sympy': ['sympy==1.4'],
    'vpython': ['vpython==7.5.2'],
    'requests': ['requests==2.18.1'],
    'psutil': ['psutil==5.6.7'],
    'opencv-python': ['opencv-python==4.1.2'],
    'beautifulsoup4': ['beautifulsoup4==4.8.1'],
    'numpy': ['numpy==1.17.2'],
    'pandas': ['pandas==0.25.1'],
    'seaborn': ['seaborn==0.9.0'],
    'scikit-learn': ['scikit-learn==0.22'],
}
py_path, py_exe = sys.executable.rsplit(os.sep, 1)  # 获取python可执行环境路径,以及可执行环境名称
os.chdir(py_path)  # 切换到对应的路径下，方便执行命令
pypi_source = "https://pypi.douban.com/simple"  # pypi源，可以根据自己的喜好进行更改

screen = turtle.Screen()
turtle.setup(800, 600)
screen.title("课程库管理（安装完成后 3 秒后自动退出）")
pen = turtle.Pen()
pen.speed(0)
pen.hideturtle()
pen.up()
pen.goto(-380, -260)
show_text = ""


def print_info(msg):
    screen.clear()
    pen.write(msg, font=("Arial", 20))


def get_LD(string_a, string_b):
    diff_start = -1
    diff_end = -1
    len_a = len(string_a)
    len_b = len(string_b)
    short = min(len_a, len_b)

    # 寻找开头和结尾的共同字符串，并记录位置
    for i in range(0, short):
        if string_a[i] != string_b[i]:
            diff_start = i
            break
    if diff_start == -1:
        return abs(len_b - len_a)
    for i in range(0, short):
        if string_a[len_a - i - 1] != string_b[len_b - i - 1]:
            diff_end = i
            break
    if diff_end == -1:
        return abs(len_b - len_a)

    # L(A+C, B+C) = LD(A, B)
    # 除去开头以及结尾相同的字符串，构建新的字符串
    long_str = str(string_a[diff_start: len_a - diff_end] if len_a >=
                   len_b else string_b[diff_start: len_b - diff_end])
    short_str = str(string_a[diff_start: len_a - diff_end] if len_a <
                    len_b else string_b[diff_start: len_b - diff_end])

    long_len = len(long_str)
    short_len = len(short_str)

    # store保存迭代过程中每次计算的结果
    store = range(0, long_len + 1)

    for i in range(short_len):
        temp = [i + 1] * (long_len + 1)
        for j in range(long_len):
            if long_str[j] == short_str[i]:
                temp[j + 1] = store[j]
            else:
                # 注意这时各个位置数据的对应关系
                temp[j + 1] = min(store[j], store[j + 1], temp[j]) + 1
        store = temp
    # 最右下角即为编辑距离
    return store[-1]


def get_osname():
    """获取操作系统名称"""
    plt = platform.platform()
    if "Darwin" in plt:
        return "Mac"
    elif "Windows" in plt:
        return "Windows"
    else:
        pass


def get_package():
    global show_text
    # 获取输入的库名及版本
    package_ = screen.textinput(
        "库管理", "请输入库名\n\n注意：指定版本时--<库名和版本中间需要加上空格>--！！！").lower()
    try:
        # 判断是否输入版本号
        if len(package_.split()) > 1:
            package_name, package_version = package_.split()
        else:
            package_name, package_version = package_, "None"
        return package_name, package_version
    except:
        show_text += "------ -> 请输入库名后，用点击Ok（或按回车）方式关闭弹窗....\n\n"
        print_info(show_text)
        print("\n------ -> 请输入库名后，用点击Ok（或按回车）方式关闭弹窗....\n\n")
        time.sleep(3)


def handle(package_name, version):
    """卸载并安装"""
    global show_text
    py_env = ".{}{}".format(os.sep, py_exe)

    os.system("{} -m pip uninstall {} -y".format(py_env, package_name))
    if version == "None":
        print("开始为您安装{} 版本！".format(package_name))
        show_text += "开始为您安装{}版本！\n\n".format(package_name)
        print_info(show_text)
        result = os.system("{} -m pip install {} -i {}".format(py_env,
                                                               package_name, pypi_source))
    else:
        print("开始为您安装{} {} 版本！".format(package_name, version))
        show_text += "开始为您安装{} {} 版本！\n\n".format(package_name, version)
        print_info(show_text)
        result = os.system("{} -m pip install {}=={} -i {}".format(py_env,
                                                                   package_name, version, pypi_source))
    if result == 0:
        if version == "None":
            print("------->  {}  版本安装成功！3 秒后自动退出...\n\n".format(package_name))
            show_text += "\n\n{}  版本安装成功! 3 秒后自动退出...\n\n".format(
                package_name)
            print_info(show_text)
            time.sleep(3)

        else:
            print("------ ->  {} {} 版本安装成功！3 秒后自动退出...\n\n".format(package_name, version))
            show_text += "\n\n{} {} 版本安装成功! 3 秒后自动退出...\n\n".format(
                package_name, version)
            print_info(show_text)
            time.sleep(3)

    else:
        # print("------ -> 安装失败，请检查名字 或 版本 是否有误 <------ -")
        # show_text += "------ -> 安装失败，请检查名字 或 版本 是否有误 <------ -\n\n"
        # print_info(show_text)
        # time.sleep(3)
        raise ValueError


def manual(package_name, package_version, common_version, osname):
    """手动安装"""
    global show_text
    # 增加判断，Mac不能用终端方式安装pyside2
    if package_name == "pyside2" and osname == "Mac":
        print("Mac系统，请在海龟编辑器的库管理中，卸载旧版，再重新安装pyside2 5.12.3")
        print_info(
            "Mac系统，请在海龟编辑器的库管理中，卸载旧版，再重新安装pyside2 5.12.3\n\n 3秒后，自动退出安装...")
        return
    print("正在卸载您电脑中已经存在的{}版本,请稍后...".format(package_name))
    show_text += "正在卸载您电脑中已经存在的{}版本,请稍后...\n\n".format(package_name)
    print_info(show_text)
    temp = []
    # 计算所有的相似度
    for i in common_version:
        temp.append([i, get_LD(package_name, i)])
    temp = sorted(temp, reverse=False, key=lambda x: x[1])
    # 如果相似度完全一致，则使用预置版本
    print(temp)
    if temp[0][1] == 0:
        print("------ ->强制指定版本")
        for i in common_version[temp[0][0]]:
            package_name, package_version = i.split("==")
            handle(package_name, package_version)
    else:
        handle(package_name, package_version)


def preset(package_name, common_version, osname):
    """预置指定版本"""
    global show_text
    # 增加判断，Mac不能用终端方式安装pyside2
    if package_name == "pyside2" and osname == "Mac":
        print("Mac系统，请在海龟编辑器的库管理中，卸载旧版，再重新安装pyside2 5.12.3")
        print_info(
            "Mac系统，请在海龟编辑器的库管理中，卸载旧版，再重新安装pyside2 5.12.3\n\n 3秒后，自动退出安装...")
        return
    print("------ -> 您输入库名或版本有误，现在开始检测是否有相似的.....")
    show_text += "您输入库名或版本有误，现在开始检测是否有相似的.....\n\n"
    print_info(show_text)
    temp = []
    # 计算所有的相似度
    for i in common_version:
        temp.append([i, get_LD(package_name, i)])
    temp = sorted(temp, reverse=False, key=lambda x: x[1])
    if temp[0][1] < 2:
        # 安装这个
        print("------ -> 存在相似的，开始重新安装...\n\n")
        show_text += "------ -> 存在相似的，开始重新安装...\n\n"
        print_info(show_text)
        print("\n存在：".format_map(common_version[temp[0][0]]))
        show_text += "\n存在：{}\n\n".format(common_version[temp[0][0]])
        print_info(show_text)
        for i in common_version[temp[0][0]]:
            package_name, package_version = i.split("==")
            manual(package_name, package_version, common_version, osname)
    else:
        print("------ -> 库名不存在，请重新运行代码，并输入正确的库名 <- ------")
        pen.goto(-380, 0)
        print_info("库名不存在，请重新运行代码，并输入正确的库名 \n\n3秒后 自动退出...")
        time.sleep(3)


if __name__ == "__main__":
    try:
        osname = get_osname()
        print("您的电脑系统为:{}".format(osname))
        show_text += "您的电脑系统为:{}\n\n".format(osname)
        print_info(show_text)
        package_name, package_version = get_package()
        try:
            manual(package_name, package_version, common_version, osname)
        except:
            preset(package_name, common_version, osname)
    except Exception as e:
        # print("安装过程出现了异常,异常信息如下:")
        # traceback.print_exc()
        show_text += "\n安装失败了\n\n"
        print_info(show_text)
        print("安装失败了,3秒后自动退出...")
        time.sleep(3)
