#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = 'my_py_note'
__author__ = 'deagle'
__date__ = '7/20/2020 10:48'
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
import numpy as np

''''
python 教程
https://www.runoob.com/python/python-basic-syntax.html

数组在内存中是引用机制

numpy.array(object, dtype = None, copy = True, order = None, subok = False, ndmin = 0)
object	数组或嵌套的数列
dtype	数组元素的数据类型，可选
copy	对象是否需要复制，可选
order	创建数组的样式，C为行方向，F为列方向，A为任意方向（默认）
subok	默认返回一个与基类类型一致的数组
ndmin	指定生成数组的最小维度
'''

# 新建数组
a = np.array([1, 2, 3])
print(a)
print(a.dtype)
print(a.shape)
print("-" * 20)

# 新建多维度数组
b = np.array([[1, 2], [3, 4]])
print(b)
print(b.shape)
print("-" * 20)

# 指定最小维度
c = np.array([1, 2, 3, 4, 5], ndmin=2)
print(c)
print(c.shape)
print("-" * 20)

if __name__ == '__main__':
    print('this message is from main function')
