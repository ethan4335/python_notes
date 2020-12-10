#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = 'my_py_note'
__author__ = 'deagle'
__date__ = '10/13/2020 21:19'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
"""
import datetime

import cv2
import numpy as np
from matplotlib import pyplot as plt

image=cv2.imread(r'D:\Anaconda\myJupyterWork\ai_traffic_flow\order_analysis\110000_20200906_destination_wangjing.png')
HSV=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
def getpos(event,x,y,flags,param):
    if event==cv2.EVENT_LBUTTONDOWN: #定义一个鼠标左键按下去的事件
        print(HSV[y,x])

cv2.imshow("imageHSV",HSV)
cv2.imshow('image',image)
cv2.setMouseCallback("imageHSV",getpos)
cv2.waitKey(0)


def main():
    print()


if __name__ == '__main__':
    start_time = datetime.datetime.now()
    main()
    end_time = datetime.datetime.now()
    time_cost = end_time - start_time
    print(str(time_cost).split('.')[0])
