# -*- coding: utf-8 -*-
'''
Author: Qin Yuan
E-mail: xiaojkql@163.com
Time: 2019-02-16 09:12:51
'''


def selectSort(ls, profier):
    for i in range(len(ls)-1, -1, -1):
        maxIndex = i
        for j in range(i-1, -1, -1):
            if ls[j] > ls[maxIndex]:
                profier.comparison()
                maxIndex = j
        profier.exchange()
        ls[maxIndex], ls[i] = ls[i], ls[maxIndex]
