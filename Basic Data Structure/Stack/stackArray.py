# -*- coding: utf-8 -*-
'''
Author: Qin Yuan
E-mail: xiaojkql@163.com
Time: 2019-02-16 22:00:38
'''

from abstractStack import AbstractStack
from arrays import Array


"""此类还有很多需要改进的地方，更好的内存管理"""


class StackArray(AbstractStack):
    DEFAULT_CAPACITY = 10

    def __init__(self, sourceCollections=None):
        self._items = Array(StackArray.DEFAULT_CAPACITY)
        AbstractStack.__init__(self, sourceCollections)

    def __iter__(self):
        for i in range(self.size()):
            yield self._items[i]

    def push(self, item):
        self._items[self.size()] = item
        self._size += 1

    def pop(self):
        if self.size() == 0:
            raise KeyError("The stack is empty")
        item = self._items[self.size()-1]
        self._size -= 1
        return item

    def peek(self):
        if self.size() == 0:
            raise KeyError("The stack is empty")
        return self._items[self.size()-1]

    def clear(self):
        self._size = 0


if __name__ == "__main__":
    stack = StackArray([1, 2, 3, 4, 5, 6])
    print(stack)
    print(stack.peek())
