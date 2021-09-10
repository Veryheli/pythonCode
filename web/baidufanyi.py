#!/usr/bin/env python
# coding=utf-8
import requests
url = 'https://fanyi.baidu.com/sug'
while True:
    src = input('输入要翻译的单词(输入q!代表退出)：')
    if src =='q!':
        break
    dat = {'kw':src}
    resp = requests.post(url,data=dat)
    tar = resp.json()
    tar = tar['data']
    print('-----------------------------------------------------------------------')
    for each in tar:
        print('单词"%s":' % each['k'])
        print('-----------翻译:%s' % each['v'])
    print('-----------------------------------------------------------------------')
    print('\n')
    resp.close()
