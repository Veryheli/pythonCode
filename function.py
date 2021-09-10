#!/usr/bin/env python
# coding=utf-8
def swap(num1,num2):
    print("in function before swap..")
    print("a = %d ,b = %d" % (num1,num2))
    num1,num2 = num2,num1
    print("in function after swap..")
    print("a = %d ,b = %d" % (num1,num2))

a = 10
b = 20 
print("out of function before swap..")
print("a = %d ,b = %d" % (a,b))
swap(a,b)
print("out of function after swap..")
print("a = %d ,b = %d" % (a,b))
