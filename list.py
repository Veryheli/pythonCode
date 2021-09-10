#!/usr/bin/env python
# coding=utf-8
#创建列表
list1 = [1,2,3,4,5]
print("-----------------------")
#使用循环改变列表中每个元素
for i in range(len(list1)):
    list1[i] *= 2
print(list1)

print("-----------------------")
#重新初始化列表
list1 = [1,2,3,4,5]
#使用列表推导式改变列表中每个元素
list1 = [i*2 for i in list1]
print(list1)

print("-----------------------")
#二维列表降级
list2 = [[1,2,3],[4,5,6],[7,8,9]]
list3 = [data for each in list2 for data in each]
print(list2)
print(list3)
