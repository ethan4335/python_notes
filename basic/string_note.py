#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = 'my_py_note'
__author__ = 'deagle'
__date__ = '7/20/2020 15:33'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
              ┏┓     ┏┓
            ┏━┛┻━━━━━┛┻━┓
            ┃     ☃     ┃
            ┃  ┳┛   ┗┳  ┃
            ┃     ┻     ┃
            ┗━┓       ┏━┛
              ┃       ┗━━━━┓
              ┃   神兽保佑  ┣┓
              ┃   永无BUG！ ┣┛
              ┗━┓┓┏━━━━┳┓┏━┛
                ┃┫┫    ┃┫┫
                ┗┻┛    ┗┻┛
"""

'''
转义字符
https://www.runoob.com/python/python-strings.html
'''

var1 = 'Hello World!'

print("输出 :- ", var1[:6] + 'Runoob!')
print()

'''
Python 字符串格式化
'''
print("My name is %s and weight is %d kg!" % ('Zara', 21))
print()

b = 'python'
print('\''+b.center(18)+'\'')
print('len: ' ,len(b.center(18)))
print(b.center(18).find('python'))

if __name__ == '__main__':
    print('this message is from main function')
