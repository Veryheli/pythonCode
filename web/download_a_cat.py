#!/usr/bin/env python
# coding=utf-8
import urllib.request
import requests
import os

size_length = input("输入你想要下载的猫的长:")
size_width= input("输入你想要下载的猫的宽:")
responce = requests.get("http://placekitten.com/"+str(size_length)+"/"+str(size_width))
cat = responce.content
if not os.path.exists("cat"):
    os.mkdir('cat')
os.chdir('cat')
with open("cat_"+str(size_length)+"_"+str(size_width)+".jpg","wb") as f:
    f.write(cat)
print("下载完毕！")
