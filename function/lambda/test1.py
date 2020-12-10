#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = 'my_py_note'
__author__ = 'deagle'
__date__ = '12/10/2020 15:25'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
"""
import datetime

def t1():
    f=lambda a,b,c,d:a*b*c*d
    print(f(1,2,3,4))  #相当于下面这个函数
    def test01(a,b,c,d):
        return a*b*c*d
    print(test01(1,2,3,4))

def t2():
    list_a = [lambda a: a ** 3, lambda b: b ** 2]
    print(list_a[0])
    g = list_a[0]
    h = list_a[1]
    # j = list_a[2]
    print(g(2))
    print(h(2))

def main():
    t1()
    t2()


if __name__ == '__main__':
    start_time = datetime.datetime.now()
    main()
    print('-' * 20)
    print('time cost: %s' % str(datetime.datetime.now() - start_time).split('.')[0])
