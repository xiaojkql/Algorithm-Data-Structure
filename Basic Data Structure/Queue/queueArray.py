# -*- coding: utf-8 -*-
'''
Author: Qin Yuan
E-mail: xiaojkql@163.com
Time: 2019-02-17 10:22:26
'''

from abstractCollections import AbstractCollections
from arrays import Array
"""底层数据结构是数组的队列的实现"""


class QueueArray(AbstractCollections):

    # constant class variable
    DEFAULT_CAPACITY = 10

    def __init__(self, sourceCollections=None):
        # 用 Array类组合成queue的类的实例变量，用来底层存储数据
        self._items = Array(QueueArray.DEFAULT_CAPACITY)
        AbstractCollections.__init__(self, sourceCollections)

    def add(self, newItem):
        self._items[self._size] = newItem
        self._size += 1

    def pop(self):
        if self.isEmpty():
            raise Exception("The queue is empty")
        popItem = self._items[0]
        self._size -= 1
        for i in range(self._size):
            self._items[i] = self._items[i+1]
        return popItem

    def peek(self):
        if self.isEmpty():
            raise Exception("The queue is empty")
        return self._items[0]

    def clear(self):
        self._size = 0

    def __iter__(self):
        for i in range(self._size):
            yield self._items[i]
