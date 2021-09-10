#!/usr/bin/env python
# coding=utf-8
from concurrent.futures import ThreadPoolExecutor
def fn(index):
    for i in range(1000):
        print(str(index)+"子线程")
#创建线程池
with ThreadPoolExecutor(50) as t:
    for i in range(100):
        t.submit(fn,index = i)
