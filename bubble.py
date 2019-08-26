#!/usr/bin/env python
# encoding: utf-8
# @software: PyCharm
# @time: 2019/8/26 11:19
# @author: Paulson●Wier
# @file: bubble.py
# @desc:

def bubbleSort(arr):
    for i in range(1, len(arr)):
        for j in range(0, len(arr)-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
        print(arr)
    return arr

if __name__ == '__main__':
    arr = [1, 0, 32, 12, 5, 76, 7]
    print(bubbleSort(arr=arr))