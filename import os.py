import os
from log import *
os.system("") #这是玄学的关键，在执行完system()之后，转移序列都会生效，原因未知
run_yes()
run_normal()

a = input("")
def print_dir(dir): 
    if(dir.find("：") == True):
        print(dir)
        Character_Error = dir.index('：')
        for i in range(Character_Error):
            print(" ",end="")
        print("^")  
        print() #使用非法字符
        Character_Error_my()
    if(dir.find("C") == True):
        print("Format error")
        Format_error()
    else:
        dir_print = f"dir {dir}"
        os.system(dir_print)

def print_tree(tree):
    if(tree.find("：") == True):
        print(tree)
        Character_Error = tree.index('：')
        for i in range(Character_Error):
            print(" ",end="")
        print("^")  
        print() #使用非法字符
        Character_Error_my()
    dir_print = f"tree {tree}"
    os.system(dir_print)

print_dir(a) 