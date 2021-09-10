#!/usr/bin/env python
# coding=utf-8
import urllib.request
responce = urllib.request.urlopen("http://www.baidu.com")
html = responce.read()
html = html.decode("utf-8")
print(html)
