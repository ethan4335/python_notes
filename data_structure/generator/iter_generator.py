#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = 'my_py_note'
__author__ = 'deagle'
__date__ = '12/10/2020 11:11'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
"""
import datetime

def fib(max):
    n,a,b =0,0,1
    while n < max:
        yield b
        a,b =b,a+b
        n = n+1
    return 'done'

def f1():
    # 无返回值调用生成器
    for i in fib(6):
        print(i)

def f2():
    # 有返回值调用生成器
    g = fib(6)
    while True:
        try:
            x = next(g)
            # print('generator: ', x)
            print(x)
        except StopIteration as e:
            print("生成器返回值：", e.value)
            break

def main():
    f1()
    print('-'*20)
    f2()





if __name__ == '__main__':
    start_time = datetime.datetime.now()
    main()
    print('-'*20)
    print('time cost: %s'%str(datetime.datetime.now() - start_time).split('.')[0])
