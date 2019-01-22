# -*- coding: utf-8 -*-
'''
Author: Qin Yuan
E-mail: xiaojkql@163.com
Time: 2019-01-22 15:42:29
'''


def indexOfMin(ls):
    """搜索列表中最小元素的index,
    如果列表为空返回-1，否则返回index"""
    if not ls:
        return -1
    minIndex = 0
    for i in range(1, len(ls)):
        if ls[minIndex] > ls[i]:
            minIndex = i
    return minIndex


if __name__ == "__main__":
    ls = [8, 4, 6, 7, 2, 5, 3, 8, 1, 5, 8, 6, 2, 4]
    print("index of min in the ls is", indexOfMin(ls))
