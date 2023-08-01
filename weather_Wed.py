import urllib.request
import gzip
import json
from Weather import broadcast

def Weather(city_name):
    city_name = ''
    wendu = []
    ganmao = []
    fengxiang = []
    fengli = []
    high = []
    low = []
    type = []
    date = []
    global city_name
    get_weather_data(city_name)
    print('------天气查询------')
    def get_weather_data(city_name) :
        url1 = 'http://wthrcdn.etouch.cn/weather_mini?city='+urllib.parse.quote(city_name)
        url2 = 'http://wthrcdn.etouch.cn/weather_mini?citykey=101010100'
        #网址1只需要输入城市名，网址2需要输入城市代码
        #print(url1)
        weather_data = urllib.request.urlopen(url1).read()
        #读取网页数据
        weather_data = gzip.decompress(weather_data).decode('utf-8')
        #解压网页数据
        weather_dict = json.loads(weather_data)
        #将json数据转换为dict数据
        return weather_dict

    def show_weather(weather_data):
        weather_dict = weather_data 
        #将json数据转换为dict数据
        if weather_dict.get('desc') == 'invilad-citykey':
            print('你输入的城市名有误，或者天气中心未收录你所在城市')
        elif weather_dict.get('desc') =='OK':
            forecast = weather_dict.get('data').get('forecast')
            print('城市：',weather_dict.get('data').get('city'))
            print('温度：',weather_dict.get('data').get('wendu')+'℃ ')
            wendu.append(weather_dict.get('data').get('wendu')+'℃')
            print('感冒：',weather_dict.get('data').get('ganmao'))
            ganmao.append(weather_dict.get('data').get('ganmao'))
            print('风向：',forecast[0].get('fengxiang'))
            fengxiang.append(forecast[0].get('fengxiang'))
            print('风级：',forecast[0].get('fengli'))
            fengli.append(forecast[0].get('fengli'))
            print('高温：',forecast[0].get('high'))
            high.append(forecast[0].get('high'))
            print('低温：',forecast[0].get('low'))
            low.append(forecast[0].get('low'))
            print('天气：',forecast[0].get('type'))
            type.append(forecast[0].get('type'))
            print('日期：',forecast[0].get('date'))
            date.append(forecast[0].get('date'))
            print('*******************************')
            for i in range(1,5):
                print('日期：',forecast[i].get('date'))
                date.append(forecast[i].get('date'))
                print('风向：',forecast[i].get('fengxiang'))
                fengxiang.append(forecast[i].get('fengxiang'))
                print('风级：',forecast[i].get('fengli'))
                fengli.append(forecast[i].get('fengli'))
                print('高温：',forecast[i].get('high'))
                high.append(forecast[i].get('high'))
                print('低温：',forecast[i].get('low'))
                low.append(forecast[i].get('low'))
                print('天气：',forecast[i].get('type'))
                type.append(forecast[i].get('type'))
                print('--------------------------')
        print('***********************************')
        print(wendu,
                ganmao,
                fengxiang ,
                fengli ,
                high ,
                low ,
                type ,
                date )
        broadcast(wendu,ganmao,fengxiang ,fengli ,high ,low ,type ,date)
    

    show_weather(get_weather_data())
