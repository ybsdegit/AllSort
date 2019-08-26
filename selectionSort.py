#!/usr/bin/env python
# encoding: utf-8
# @software: PyCharm
# @time: 2019/8/26 13:44
# @author: Paulson●Wier
# @file: selectionSort.py
# @desc:


def select_sort(arr):
    for i in range(len(arr)-1):
       # 记录最小数的索引
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        # i 不是最小数时， 将i和最小数进行交换
        if i != min_index:
            arr[i], arr[min_index] = arr[min_index], arr[i]
            print(arr)
    return arr


if __name__ == '__main__':
    arr = [1, 0, 32, 12, 5, 76, 7]
    print(select_sort(arr=arr))




