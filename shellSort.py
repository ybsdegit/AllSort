#!/usr/bin/env python
# encoding: utf-8
# @software: PyCharm
# @time: 2019/8/26 14:14
# @author: Paulson●Wier
# @file: shellSort.py
# @desc: 希尔排序

def shell_sort(arr):
    import math
    gap = 1
    while(gap < len(arr)/3):
        gap = gap*3+1
    while gap > 0:
        for i in range(gap, len(arr)):
            temp = arr[i]
            j = i - gap
            while j >= 0 and arr[j] > temp:
                arr[j+gap] = arr[j]
                j-=gap
            arr[j + gap] = temp
        gap = math.floor(gap/3)
    return arr

if __name__ == '__main__':
    arr = [1, 0, 32, 12, 5, 76, 7]
    print(shell_sort(arr=arr))
