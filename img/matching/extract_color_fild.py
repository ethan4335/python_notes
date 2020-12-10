#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = 'my_py_note'
__author__ = 'deagle'
__date__ = '10/13/2020 21:11'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
"""
import datetime

import cv2
import numpy as np

# 读取名称为 opencvlogo.png的图片
img = cv2.imread(r'D:\Anaconda\myJupyterWork\ai_traffic_flow\order_analysis\110000_20200906_destination_wangjing.png', 1)

# 将图片转换为格式 hsv
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# 定义蓝色的上下限
lower_blue = np.array([0,0,0])
higher_blue = np.array([255,200,220])

# 在图片中提取蓝色的部分
mask = cv2.inRange(hsv, lower_blue, higher_blue)

# 和原图像求“与”操作，只保留蓝色
left_blue = cv2.bitwise_and(img, img, mask=mask)

# 显示hsv
cv2.imshow("P3-OpenCV logo", img)
# 显示Blue
cv2.imshow("P3-Blue", left_blue)

cv2.waitKey(0)

def main():
    print()


if __name__ == '__main__':
    start_time = datetime.datetime.now()
    main()
    end_time = datetime.datetime.now()
    time_cost = end_time - start_time
    print(str(time_cost).split('.')[0])
