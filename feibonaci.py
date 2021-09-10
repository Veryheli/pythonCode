#!/usr/bin/env python
# coding=utf-8
def feibonaci(n):
    if n ==1 or n ==2:
        return 1
    elif n <= 0:
        print("数据错误！")
    else:
        return feibonaci(n-1)+feibonaci(n-2)
for n in range(1,20):
    print("非波那契数列第%d项为%d" % (n,feibonaci(n)))
