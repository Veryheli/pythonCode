#!/usr/bin/env python
# coding=utf-8
class Person:
    def __init__(self,name ,age):
        self.name = name
        self.age = age
    def show(self):
        print("name:"+self.name)
        print("age:"+str(self.age))
