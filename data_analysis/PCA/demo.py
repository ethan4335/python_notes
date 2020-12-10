#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = 'my_py_note'
__author__ = 'deagle'
__date__ = '12/1/2020 20:56'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
"""
import datetime
import numpy as np
from sklearn.decomposition import PCA

def test1():
    X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
    pca = PCA(n_components=2)
    pca.fit(X)
    # PCA(copy=True, n_components=2, whiten=False)
    print(pca.explained_variance_ratio_)

def test2():
    X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
    pca = PCA(n_components='mle')
    pca.fit(X)
    # PCA(copy=True, n_components=2, whiten=False)
    print(pca.explained_variance_ratio_)

def main():
    test1()
    test2()


if __name__ == '__main__':
    start_time = datetime.datetime.now()
    main()
    print('time cost: ',str(datetime.datetime.now() - start_time).split('.')[0])
