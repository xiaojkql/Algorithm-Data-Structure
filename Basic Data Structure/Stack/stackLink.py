# -*- coding: utf-8 -*-
'''
Author: Qin Yuan
E-mail: xiaojkql@163.com
Time: 2019-02-16 22:17:36
'''

from node import Node
from abstractStack import AbstractStack


class StackLink(AbstractStack):
    def __init__(self, sourceCollections=None):
        self._items = None
        AbstractStack.__init__(self, sourceCollections)

    def __iter__(self):
        probe = self._items
        while probe is not None:
            yield probe._data
            probe = probe._next

    def push(self, item):
        self._items = Node(item, self._items)
        self._size += 1

    def peek(self):
        if self.isEmpty():
            raise KeyError("Stack is empty")
        return self._items._data

    def pop(self):
        if self.isEmpty():
            raise KeyError("Stack is empty")
        item = self._items._data
        self._items = self._items._next
        self._size -= 1
        return item


if __name__ == "__main__":
    stack = StackLink([4, 7, 2, 100, 200])
    for item in stack:
        print(item)
