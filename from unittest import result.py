from unittest import result
import requests
from lxml import etree
import re

url = "https://www.bilibili.com/video/BV1t34y1q7vf"
header = {

}

result = requests.get(url,headers=header).text
dom = etree.HTML(result)
movie_urls = dom.xpath('//h4[@class="video-name one-line"]/a[@href]/@href')
movie_names = dom.xpath('//h4[@class="video-name one-line"]/a[@href]/text()')
for movie_url,movie_name in zip(movie_urls,movie_names):
    print(movie_url,movie_name)
    movie_id_string = requests.get(movie_url).text
    movie_mp4_url = re.search('source src="(.*)"type',movie_id_string).group(1)
    print(movie_mp4_url)
    mp4 = requests.get(movie_mp4_url).content
    with open('./movie/%s.mp4'%movie_name,'wb') as data_file:
        data_file.write(mp4)
