#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = 'my_py_note'
__author__ = 'deagle'
__date__ = '10/13/2020 18:13'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
"""
import datetime



'''
don't work
'''
import cv2
import numpy as np

if __name__ == "__main__":
    img = cv2.imread(r'D:\Anaconda\myJupyterWork\ai_traffic_flow\order_analysis\110000_20200906_destination_wangjing.png')
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)  # 色彩空间转换为hsv，分离.

    # 色相（H）是色彩的基本属性，就是平常所说的颜色名称，如红色、黄色等。
    # 饱和度（S）是指色彩的纯度，越高色彩越纯，低则逐渐变灰，取0-100%的数值。
    # 明度（V），取0-100%。
    # OpenCV中H,S,V范围是0-180,0-255,0-255
    # 249 58 67
    low = np.array([175, 63, 255])
    high = np.array([180, 66, 255])

    dst = cv2.inRange(src=hsv, lowerb=low, upperb=high)  # HSV高低阈值，提取图像部分区域

    # 寻找白色的像素点坐标。
    # 白色像素值是255，所以np.where(dst==255)
    xy = np.column_stack(np.where(dst == 255))
    print(xy)

    # 在原图的红色数字上用 金黄色 描点填充。
    for c in xy:
        print(c)
        # 注意颜色值是(b,g,r)，不是(r,g,b)
        # 坐标:c[1]是x,c[0]是y
        cv2.circle(img=img, center=(int(c[1]), int(c[0])), radius=1, color=(255, 63, 255), thickness=1)

    cv2.imshow('dst', dst)
    # cv2.imshow('result', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


