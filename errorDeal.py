#!/usr/bin/env python
# coding=utf-8
file_name = input("输入要打开的文件名：")
try:
    file = open(file_name)
    for each_line in file:
        print(each_line)
    file.close()
except OSError:
    print("文件不存在！")
