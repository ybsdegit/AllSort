#!/usr/bin/env python
# encoding: utf-8
# @software: PyCharm
# @time: 2019/8/26 14:39
# @author: Paulson●Wier
# @file: quickSort.py
# @desc: 快速排序

def quick_sort(arr, left=None, right=None):
    left = 0 if not isinstance(left, (int, float)) else left
    right = len(arr)-1 if not isinstance(right, (int, float)) else right
    if left < right:
        partitionIndex = partition(arr, left, right)
        quick_sort(arr, left, partitionIndex - 1)
        quick_sort(arr, partitionIndex + 1, right)
    return arr


def partition(arr, left, right):
    pivot = left
    index = pivot+1
    i = index
    while  i <= right:
        if arr[i] < arr[pivot]:
            swap(arr, i, index)
            index+=1
        i+=1
    swap(arr,pivot,index-1)
    return index-1

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]