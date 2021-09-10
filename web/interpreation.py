#!/usr/bin/env python
# coding=utf-8
import urllib.request
import urllib.parse
import json

url = 'https://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
head = {}
head['User-Agent'] = 'Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0'

src = input("输入要翻译的内容：")

data = {}
data['i']= src
data['from']="AUTO"
data['to']= "AUTO"
data['smartresult']= "dict"
data['client'] = "fanyideskweb"
data["salt"]= "16296053490966"
data["sign"]= "51eb52ae416e863faf0f29229f8b5a2d"
data["lts"]= "1629605349096"
data["bv"]= "1de9313c44872e4c200c577f99d4c09e"
data["doctype"]= "json"
data["version"]= "2.1"
data["keyfrom"]= "fanyi.web"
data["action"]= "FY_BY_CLICKBUTTION"

data = urllib.parse.urlencode(data).encode('utf-8')

request = urllib.request.Request(url,data,head)
responce = urllib.request.urlopen(request)

html = responce.read().decode('utf-8')
html = json.loads(html)

print("翻译结果："+html['translateResult'][0][0]['tgt'])
