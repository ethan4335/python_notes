#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = 'my_py_note'
__author__ = 'deagle'
__date__ = '10/12/2020 16:37'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
"""

import datetime
from typing import List


def search(nums: List[int], target: int) -> int:
    low = 0
    high = len(nums) - 1
    while low <= high:
        mid = low + ((high - low) >> 1)
        if nums[mid] == target:
            return mid
        elif nums[mid] < nums[low]:
            if target >= nums[mid] and target <= nums[high]:
                low = mid
            else:
                high = mid - 1
        else:
            if target >= nums[low] and target <= nums[mid]:
                high = mid
            else:
                low = mid + 1
    return -1


def main():
    list2 = [6, 7, 7, 7, 7, 7, 12, 13, 14, 15, 1, 2, 3, 4, 5]
    res = search(list2, 12)
    print(res)


if __name__ == '__main__':
    start_time = datetime.datetime.now()
    main()
    end_time = datetime.datetime.now()
    time_cost = end_time - start_time
    print(str(time_cost).split('.')[0])
