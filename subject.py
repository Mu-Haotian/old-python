

star_12 = ("白羊座", "金牛座", "双子座", "巨蟹座", "狮子座", "处女座",
           "天枰座", "天蝎座", "射手座", "摩羯座", "水瓶座", "双鱼座") 
blood = ("A型", "B型", "AB型", "O型","a","b","ab","o","hr阴性","hr阳性")

yearbook = []
print("=========================================欢迎使用同学录=====================================================") 

class alumni_book:
  def name():
    while True:
      judge = 1 
      name = ''
      name_complete = ''
      name_len = ''
      print("ps:最长4个字,最短1个字,不可以输入数字和符号")
      name = input("姓名")
      name_len = len(name)
      if name_len <= 1:
        print("太短了")
        print("请重新输入")
        judge = 0 
      elif name_len >= 5:
        print("太长了")
        print("请重新输入")
        judge = 0
      elif judge == 1:
        name_complete = name
        break   

  def nickname():
    while True:
      judge = 1 
      nickname = ''
      nickname_complete = ''
      nickname_len = ''
      print("ps:最长10个字,最短2个字,不可以输入数字和符号;不填也可以直接输入空格")
      nickname = input("昵称")
      nickname_len = len(nickname)
      #name_digit(name)
      if nickname == ' ':
        judge = 1 
      if nickname_len <= 1:
        print("太短了")
        print("请重新输入")
        judge = 0 
      if nickname_len >= 10:
        print("太长了")
        print("请重新输入")
        judge = 0
      elif judge == 1:
        nickname_complete = nickname
        break   

  def blood():
    print("ps:有白羊座, 金牛座, 双子座, 巨蟹座, 狮子座, 处女座,天枰座, 天蝎座, 射手座, 摩羯座, 水瓶座, 双鱼座。只准输入有效的")
    blood_4  = input("血型:")
    while blood_4 not in blood:
        print("这是什么血型？")
        blood_4  = input("血型:")

  print
  name()
  nickname()
  blood()



