#!/usr/bin/env python
# coding=utf-8
count = 0
def hanoi(step,start,assistant,target):
    if step == 1:
        print("{}->{}".format(start,target))
    else:
        hanoi(step-1,start,target,assistant)
        print("{}->{}".format(start,target))
        hanoi(step-1,assistant,start,target)
step = input("请输入汗诺塔的层数:")
hanoi(int(step),'A','B','C')
