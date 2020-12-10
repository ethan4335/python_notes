#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = 'my_py_note'
__author__ = 'deagle'
__date__ = '12/10/2020 11:27'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
"""
import datetime


def foo():
    print("starting...")
    while True:
        res = yield 4
        print("res:",res)


def main():
    g = foo()
    print(next(g))
    print("*" * 20)
    print(next(g))

    print('-'*20)

    g = foo()
    print(next(g))
    print("*" * 10)
    print(g.send(7))


if __name__ == '__main__':
    start_time = datetime.datetime.now()
    main()
    print('-'*20)
    print('time cost: %s'%str(datetime.datetime.now() - start_time).split('.')[0])
