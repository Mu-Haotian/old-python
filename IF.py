from weather import Weather

def question():
    print("在以下输入问题")
    issue = input("")

    if issue == "天气" :
        Weather()

    if issue == "天气预报" :
        Weather()

    

    else:
        print("无法回答")

        