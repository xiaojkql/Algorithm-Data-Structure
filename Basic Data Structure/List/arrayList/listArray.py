# -*- coding: utf-8 -*-
'''
Author: Qin Yuan
E-mail: xiaojkql@163.com
Time: 2019-02-17 19:10:53
'''

from arrays import Array
from abstractList import AbstractList


class ListArray(AbstractList):
    DEFAULT_CAPACITY = 10

    def __init__(self, sourceCollections=None):
        self._items = Array(ListArray.DEFAULT_CAPACITY)
        AbstractList.__init__(self, sourceCollections)

    def __iter__(self):
        for i in range(len(self)):
            yield self._items[i]

    def __getitem__(self, index):
        if index < 0 or index >= len(self):
            raise IndexError("List index out of range")
        return self._items[index]

    def __setitem__(self, index, item):
        if index < 0 or index >= len(self):
            raise IndexError("List index out of range")
        self._items[index] = item

    def insert(self, index, item):
        if index < 0:
            index = 0
        if index > len(self):
            index = len(self)
        for i in range(len(self), index, -1):
            self._items[i] = self._items[i-1]
        self._items[index] = item
        self._size += 1
        self.incModCount()

    def pop(self, index=None):
        if index is None:
            index = len(self)-1
        if index < 0 or index >= len(self):
            raise IndexError("List index outof range")
        popItem = self._items[index]
        for i in range(index, len(self)-1):
            self._items[i] = self._items[i+1]
        self._size -= 1
        self.incModCount()
        return popItem


# simple test
def main():
    ls = ListArray([7, 8, 9, 5, 10])
    print(ls)
    print(ls.pop())
    print(ls.pop(2))
    ls.insert(2, 1000)
    print(ls)


if __name__ == "__main__":
    main()
