#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = 'my_py_note'
__author__ = 'deagle'
__date__ = '7/20/2020 16:54'
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
含有时间计算，日历计算，日历显示，时间显示
https://www.runoob.com/python/python-date-time.html
'''

import time

localtime = time.localtime(time.time())
print("本地时间为 :", localtime)

# 格式化时间
localtime = time.asctime( time.localtime(time.time()) )
print("本地时间为 :", localtime)

'''
常用时间格式： %Y-%m-%d %H:%M:%S
'''
# 格式化成2016-03-20 11:45:39形式
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))


# 格式化成Sat Mar 28 22:24:24 2016形式
print(time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()))


# 将格式字符串转换为时间戳
a = "Sat Mar 28 22:24:24 2016"
print(time.mktime(time.strptime(a, "%a %b %d %H:%M:%S %Y")))

'''
还可以获得整个日历
'''

import calendar

cal = calendar.month(2020, 7)
print("以下输出2020年7月份的日历:")
print(cal)


if __name__ == '__main__':
    print('this message is from main function')