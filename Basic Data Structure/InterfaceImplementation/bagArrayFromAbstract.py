# -*- coding: utf-8 -*-
'''
Author: Qin Yuan
E-mail: xiaojkql@163.com
Time: 2019-02-16 20:32:35
'''

from abstractClass import AbstractBag
from arrays import Array


class BagArray(AbstractBag):
    DEFAULT_CAPACITY = 10

    def __init__(self, sourceCollections=None):
        self._items = Array(BagArray.DEFAULT_CAPACITY)
        AbstractBag.__init__(self, sourceCollections)

    def __iter__(self):
        for i in range(self._size):
            yield self._items[i]

    def add(self, item):
        self._items[len(self)] = item
        self._size += 1


if __name__ == "__main__":
    bag = BagArray([1, 2, 3, 4, 5, 6])
    print(bag)
