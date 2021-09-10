#!/usr/bin/env python
# coding=utf-8
import requests
url = 'http://www.baidu.com'
myHeader = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0'}
resp = requests.get(url,headers = myHeader)
with open('baidu.html','w') as f:
    f.write(resp.text)
