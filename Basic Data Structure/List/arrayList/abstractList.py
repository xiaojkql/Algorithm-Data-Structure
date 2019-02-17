# -*- coding: utf-8 -*-
'''
Author: Qin Yuan
E-mail: xiaojkql@163.com
Time: 2019-02-17 19:03:44
'''

from abstractCollections import AbstractCollections


class AbstractList(AbstractCollections):
    def __init__(self, sourceCollections):
        self._modCount = 0
        AbstractCollections.__init__(self, sourceCollections)

    def getModCount(self):
        return self._modCount

    def incModCount(self):
        self._modCount += 1

    def index(self, item):
        position = 0
        for target in self:
            if target == item:
                return position
            position += 1
        if position == len(self):
            raise ValueError(str(item)+" not in list")

    def add(self, item):
        self.insert(len(self), item)

    def remove(self, item):
        position = self.index(item)
        self.pop(position)
