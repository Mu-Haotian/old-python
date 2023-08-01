import math
from numbers import Number
class mode():
    def addition(self):
        #加法
        self.addition1 = int(input("第一个加数"))
        self.addition2 = int(input("第二个加数"))
        self.additio_number = (self.addition1 + self.addition2) # 加数 + 加数 = 得数
        print("得数是:" + str(self.additio_number)) #得数打印
        print("")
    
    def Lianjia(self):
        #连加
        self.addition1_list = []
        self.frequency = 0
        
        self.frequency = input("多少个加数")
        for i in range(self.frequency):
            self.addition1_list
    
    def subtraction(self):
        #减法
        self.subtraction1 = int(input("第一个减数"))
        self.subtraction2 = int(input("第二个减数"))
        self.subtraction_number = (self.subtraction1 - self.subtraction2) # 减数 - 减数 = 得数
        print("得数是:" + str(self.subtraction_number)) #得数打印
        print("")
    
    def multiplication(self):
        #乘法
        self.multiplication1 = int(input("第一个乘数"))
        self.multiplication2 = int(input("第二个乘数"))
        self.multiplication_number = (self.multiplication1 * self.multiplication2) # 乘数 * 乘数 = 得数
        print("得数是:" + str(self.multiplication_number)) #得数打印
        print("")

    def division(self):
        #除法
        self.division1 = int(input("第一个除数"))
        self.division2 = int(input("第二个除数"))
        self.division_number = (self.division1 / self.division2)
        self.round = input("需要四舍五入吗？ ps:回答yes或no:")
        if self.round == "yes":
            self.number = int(input("舍入几位?:"))
            self.division_round = round(self.division_number,self.number)
            print("得数是:" + str(self.division_round)) #得数打印
            print("")
        if self.round == "no":
            print("得数是:" + str(self.division_number)) #得数打印
            print("")
    
    def Even_multiply(self):
        #连乘
        self.Even_multiply1 = int(input("起数"))
        self.Even_multiply2 = int(input("结数"))
        self.All_numbers = range(self.Even_multiply1,self.Even_multiply2)
        self.Even_multiply_number = sum(self.All_numbers) + self.Even_multiply2
        print("得数是:" + str(self.Even_multiply_number))
        print("")
    
    def prime_number(self):
        print("注意0和1既不是和数也不是质数")
        self.prime = eval(input('请输入判断数字:'))
        if self.prime<=1:
            print('这不是质数')
        elif self.prime==2:
            print('这是一个质数!')
        else:
            i=2
            while i<self.prime:
                if self.prime%i==0:
                    print('这不是一个质数')
                    break
                i=i+1
            else:
                print ('这是一个质数!')
    
    def Composite_number(self):
        print("注意0和1既不是和数也不是质数")
        self.Composite = eval(input('请输入判断数字:'))
        if self.prime<=1:
            print('这是和数')
        elif self.prime==2:
            print('这是不是和数!')
        else:
            i=2
            while i<self.prime:
                if self.prime%i==0:
                    print('这是一个和数')
                    break
                i=i+1
            else:
                print ('这不是一个和数!')
    
    def size(self):
        list1 = ['零', '壹', '贰', '叁', '肆', '伍', '陆', '柒', '捌', '玖', '拾']
        list2 = ['圆', '拾', '佰', '仟', '萬']
        
        self.money = str(int(input("请输入数字:")))  # 预防输入0开头的数字
        self.money2 = ''
        for i in range(0, len(self.money)):
            if int(self.money[i]) != 0:
                self.money2 += list1[int(self.money[i])] + list2[len(self.money) - i - 1]
            else:
                if self.money2[-1] != "零":
                    self.money2 += "零"
        if self.money2[-1] == "零":
            print(self.money2[0:len(self.money2) - 1] + "圆整")
        else:
            print(self.money2 + "整")

    
class Operation():
    # 0 == 0 卡无限循环
    while 0 == 0:
        Operation_mode = input("运算方式:")
        if Operation_mode == "加法":
            mode().addition()
        
        if Operation_mode == "减法":
            mode().subtraction()

        if Operation_mode == "乘法":
            mode().multiplication()

        if Operation_mode == "除法":
            mode().division()
        
        if Operation_mode == "连乘":
            mode().Even_multiply()
        
        if Operation_mode == "质数判断":
            mode().prime_number()
        
        if Operation_mode == "和数判断":
            mode().Composite_number()

        if Operation_mode == "小写转大写":
            mode().size()

if __name__ == '__main__':
    calculator = Operation()
