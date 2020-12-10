#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = 'my_py_note'
__author__ = 'deagle'
__date__ = '7/20/2020 15:44'
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
[]
'''

list1 = ['physics', 'chemistry', 1997, 2000]
list2 = [1, 2, 3, 4, 5, 6, 7]
list3 = [2, 3, 4, 5, 2, 2, 1]

print("list1[0]: ", list1[0])

print("list2[1:5]: ", list2[1:5])

list = []  ## 空列表
list.append('Google')  ## 使用 append() 添加元素
list.append('Runoob')
list.append('vasdawfwefa')
print(list)
del list[2]
print(list)

print()
print( (list3 < list2) - (list3 > list2))
print()

# 列表
vowels = ['e', 'a', 'u', 'o', 'i']
nums = [22,33,66,11,55]
# 降序
vowels.sort(reverse=True)
nums.sort()

# 输出结果
print('降序输出:', vowels)
print('正序输出:', nums)

print()
'''
指定按照第二列进行整体排序
'''


# 获取列表的第二个元素
def takeSecond(elem):
    return elem[1]


# 列表
random = [(2, 2), (3, 4), (4, 1), (1, 3)]

# 指定第二个元素排序
random.sort(key=takeSecond)

# 输出类别
print('排序列表：', random)


if __name__ == '__main__':
    print('this message is from main function')
