#!/usr/bin/env python
# coding=utf-8
from threading import Thread
class MyThread(Thread):
    def setname(self,name):
        self.name = name
    def run(self):
        for i in range(1000000):
            print('{} is running..'.format(self.name))

if __name__ == '__main__':
    for i in range(10):
        t = MyThread()
        t.setname(i)
        t.start()
