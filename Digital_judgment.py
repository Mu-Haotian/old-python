from Data_type_judgment import Type_judgment
def name_digit(data):
    for digit in range(10000):
        Type_judgment(digit)
        digit = int(digit)
        if data.find(digit) == 0:
            print("不支持数字")
            print("请重新输入")
        print(data.find("digit"))
        digit = ''