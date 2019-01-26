# -*- coding: utf-8 -*-
'''
Author: Qin Yuan
E-mail: xiaojkql@163.com
Time: 2019-01-26 12:03:17
'''


def insertSort(ls, lo, hi):
    """insertSort for list
    思想：前i个项排序好，将第i+1项按照顺序插入到前i项中"""
    for i in range(lo+1, hi):
        temp = ls[i]
        j = i-1
        while j >= 0:
            if ls[j] > temp:
                ls[j+1] = ls[j]
                j -= 1
            else:
                break
        ls[j+1] = temp


if __name__ == "__main__":
    ls = [1, 4, 2, 7, 5, 3]
    insertSort(ls, 0, len(ls))
    print(ls)
