# -*- coding: utf-8 -*-
'''
Author: Qin Yuan
E-mail: xiaojkql@163.com
Time: 2019-01-22 15:55:49
'''


def binarySearch(ls, target):
    """针对有序列表的二分查找方法，
    找到返回index,否则-1"""
    lo, hi = 0, len(ls)  # [lo,hi)
    while lo < hi:
        mid = (lo+hi)//2
        if ls[mid] == target:
            return mid
        elif target < ls[mid]:
            hi = mid
        else:
            lo = mid+1
    return -1


if __name__ == "__main__":
    ls = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(binarySearch(ls, 3))
    print(binarySearch(ls, 100))
