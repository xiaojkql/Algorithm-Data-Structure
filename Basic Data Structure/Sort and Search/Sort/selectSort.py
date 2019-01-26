# -*- coding: utf-8 -*-
'''
Author: Qin Yuan
E-mail: xiaojkql@163.com
Time: 2019-01-26 11:46:27
'''


def selectSort(ls, lo, hi):
    """selectSort for list"""
    while lo < hi-1:
        minIndex = lo
        for i in range(lo+1, hi):
            if ls[i] < ls[minIndex]:
                minIndex = i
        ls[lo], ls[minIndex] = ls[minIndex], ls[lo]
        lo += 1


if __name__ == "__main__":
    ls = [1, 4, 2, 5, 7, 83, 4, 6, 7]
    selectSort(ls, 0, len(ls))
    print(ls)
