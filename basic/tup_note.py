#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = 'my_py_note'
__author__ = 'deagle'
__date__ = '7/20/2020 15:53'
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
元组与字符串类似，下标索引从0开始，可以进行截取，组合等。
'''

tup1 = ('physics', 'chemistry', 1997, 2000)
tup2 = (1, 2, 3, 4, 5, 6, 7)

print("tup1[0]: ", tup1[0])

print("tup2[1:5]: ", tup2[1:5])

'''
任意无符号的对象，以逗号隔开，默认为元组，
'''
print ('abc', -4.24e93, 18+6.6j, 'xyz')
x, y = 1, 2
print ("Value of x , y : ", x,y)

'''
相对于 list 而言，tuple 是不可变的，这使得它可以作为 dict 的 key，或者扔进 set 里，而 list 则不行。
tuple 放弃了对元素的增删（内存结构设计上变的更精简），换取的是性能上的提升：创建 tuple 比 list 要快，
存储空间比 list 占用更小。所以就出现了“能用 tuple 的地方就不用 list”的说法。
'''

'''
元祖间接修改
'''

tup1 = (12, 34.56)
tup2 = ('abc', 'xyz')

# 创建一个新的元组
tup3 = tup1 + tup2
print(tup3)



if __name__ == '__main__':
    print('this message is from main function')