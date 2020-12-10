#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = 'my_py_note'
__author__ = 'deagle'
__date__ = '12/7/2020 19:42'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
"""
import datetime
import numpy as np
import torch


def main():

    np_arr = np.array([[1, 2, 3, 4],[5, 6, 7, 8]])
    tor_arr = torch.from_numpy(np_arr)
    tor2numpy = tor_arr.numpy()
    print('\nnumpy\n', np_arr, '\ntorch\n', tor_arr, '\nnumpy\n', tor2numpy)


if __name__ == '__main__':
    start_time = datetime.datetime.now()
    main()
    print(str(datetime.datetime.now() - start_time).split('.')[0])
