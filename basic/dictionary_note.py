#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = 'my_py_note'
__author__ = 'deagle'
__date__ = '7/20/2020 16:49'
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

#创建字典
dict1 = { 'abc': 456 }
dict2 = { 'abc': 123, 98.6: 37 }

dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

print("dict['Name']: ", dict['Name'])
print("dict2[98.6]: ", dict2[98.6])

'''
字典值可以没有限制地取任何python对象，既可以是标准的对象，也可以是用户定义的，但键不行。

注意！！！
键必须不可变，所以可以用数字，字符串或元组充当，所以用列表就不行。
'''

dict = {('Name','s'): 'Zara', 'Age': 7}

print("dict['Name','s']: ", dict[('Name','s')])


if __name__ == '__main__':
    print('this message is from main function')