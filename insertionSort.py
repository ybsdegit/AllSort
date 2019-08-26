#!/usr/bin/env python
# encoding: utf-8
# @software: PyCharm
# @time: 2019/8/26 14:02
# @author: Paulson●Wier
# @file: insertionSort.py
# @desc: 插入排序

def insertion_sort(arr):
    for i in range(len(arr)):
        pre_index = i-1
        current = arr[i]
        while pre_index >=0 and arr[pre_index] > current:
            arr[pre_index+1] = arr[pre_index]
            pre_index -= 1
        arr[pre_index+1] = current
    return arr

if __name__ == '__main__':
    arr = [1, 0, 32, 12, 5, 76, 7]
    print(insertion_sort(arr=arr))


