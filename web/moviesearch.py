#!/usr/bin/env python
# coding=utf-8
import requests
import re

class Movie:
    base_url = 'https://miao101.com/search?q='
    myHeaders = {'user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'}
    resourses_urls = []
    def __init__(self):
        self.run()
    def run(self):
       self.resourses_urls = self.search()
    def search(self):#搜索后获取页面资源url将其储存在列表中
        searchTarget = input('输入你要查询的影视：')
        url = self.base_url + searchTarget
        resp = requests.get(url,headers = self.myHeaders)
        # result = re.search(r'<div class="my-3">(?P<result>.*?)</div>',resp.text)
        # print(result.group('result'))#搜索的结果,显示又几条结果
        print('搜索结果如下：')
        resourse_urls_tails = re.finditer(r'<a href="(?P<url_tails>.*?)" target="_blank" class="text-dark"><b>(?P<name>.*?)</b></a>',resp.text)
        resourses_urls_frames = []
        resourse_name = []
        for i in resourse_urls_tails:
            resourse_name.append(i.group('name'))
            resourses_urls_frames.append('http://miao101.com'+i.group('url_tails'))
        for i in range(len(resourses_urls_frames)):
            print(resourse_name[i],resourses_urls_frames[i])

if __name__ == '__main__':
    m = Movie()
