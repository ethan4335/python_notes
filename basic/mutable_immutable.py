#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = 'my_py_note'
__author__ = 'deagle'
__date__ = '7/20/2020 17:03'
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
python 传不可变对象实例
'''
def ChangeInt(a):
    a = 10

b = 2
ChangeInt(b)
print('不可变：',b) # 结果是 2
print()

'''
传可变对象实例
'''

# 可写函数说明


def changeme(mylist):
    "修改传入的列表"
    mylist.append([1, 2, 3, 4])
    print("函数内取值: ", mylist)

    return


# 调用changeme函数
mylist = [10, 20, 30]
changeme(mylist)
print("函数外取值: ", mylist)



if __name__ == '__main__':
    print('this message is from main function')