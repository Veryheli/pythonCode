#!/usr/bin/env python
# coding=utf-8
import requests
import re
class Weather:
    base_url = 'http://www.weather.com.cn'
    head = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'}
    def __init__(self):
        self.run()
    def get_weather_details(self,city_urls):
        #通过city_urls的界面提取详细的天气信息
        time = re.compile('<input type="hidden" id="fc_24h_internal_update_time" value="(?P<time>.*?)"/>')
        tem = re.compile('<input type="hidden" id="hidden_title" value="(?P<tem>.*?)" />')
        resp = requests.get(city_urls,headers = self.head)#确保能够正确显示结果
        resp.encoding = resp.apparent_encoding
        tar = tem.search(resp.text).group('tem').split('  ')
        print('更新时间：{}'.format(time.search(resp.text).group('time')))
        print('天气：')
        for i in range(len(tar) - 1):
            print(tar[i+1])
    def input_city(self):
        url = 'http://toy1.weather.com.cn/search?cityname='
        city_name = input('输入要查询的城市：')
        url = url + city_name
        resp = requests.get(url,headers = self.head)
        target = resp.text
        city_id = re.findall(r'ref":"(?P<city_id>.*?)~',target)#这里的city_id是一个列表，记录了所有与搜索相关的城市的id
        resp.close()
        # print(city_id)
        #http://www.weather.com.cn/weather1d/101020100.shtml#input
        city_urls = []
        for id in city_id:
            city_urls.append('http://www.weather.com.cn/weather1d/' + id +'.shtml#input' )
        # for i in range(len(city_urls)):
        #     print(city_urls[i])
        return city_urls[0] #为避免空页面，返回与搜索结果最近的url
    def run(self):
        city_urls = self.input_city()
        self.get_weather_details(city_urls)
if __name__ == '__main__':
    w = Weather()
