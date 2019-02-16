# -*- coding: utf-8 -*-
'''
Author: Qin Yuan
E-mail: xiaojkql@163.com
Time: 2019-02-16 19:49:21
'''

from bagArray import BagArray


class SortedBag(BagArray):
    def __init__(self, sourceCollections=None):
        BagArray.__init__(self, sourceCollections)

    def add(self, item):
        if item > self._item[len(self)]:
            BagArray.add(item)
        targetIndex = 0
        while item < self._item[targetIndex]:  # 在不确定循环次数时尽量多实用while,避免使用break
            targetIndex += 1
        for i in range(len(self), targetIndex, -1):
            self._item[i] = self._item[i-1]
        self._item[targetIndex] = item
        self._size += 1

    def __contains__(self, item):
        lo = 0
        hi = len(self)
        while lo < hi:
            mi = (lo + hi) // 2
            if self._item[mi] == item:
                return True
            elif self._item[mi] > item:
                hi = mi
            else:
                lo = mi
        return False
