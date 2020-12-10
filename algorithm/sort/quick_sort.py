#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = 'my_py_note'
__author__ = 'deagle'
__date__ = '7/20/2020 10:43'
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

# quicksort
def quicksort(arr):
  if len(arr) <=1:
      return arr
  pivot = arr[len(arr) // 2]
  left = [x for x in arr if x < pivot]
  middle = [x for x in arr if x == pivot]
  right = [x for x in arr if x > pivot]
  return  quicksort(left) + middle + quicksort(right)

print(quicksort([3,6,8,10,1,2,1]))
# output: [1, 1, 2, 3, 6, 8, 10]

if __name__ == '__main__':
    print('this message is from main function')