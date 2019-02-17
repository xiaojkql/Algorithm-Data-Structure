# -*- coding: utf-8 -*-
'''
Author: Qin Yuan
E-mail: xiaojkql@163.com
Time: 2019-02-17 10:48:29
'''

# 底层存储数据项的数据结构为链表实现的队列
from abstractCollections import AbstractCollections
from node import Node


class QueueLink(AbstractCollections):
    def __init__(self, sourceCollections=None):
        # 借助两个实例变量来记录队头和队尾
        self._front = None
        self._rear = None
        AbstractCollections.__init__(self, sourceCollections)

    def add(self, newItem):
        newNode = Node(newItem, None)
        if self._front is None:
            self._front = newNode
        else:
            self._rear._next = newNode
        self._rear = newNode
        self._size += 1

    def pop(self):
        if self.isEmpty():
            raise KeyError("Queue is empty!")
        popItem = self._front._data
        if self._front._next is None:
            self._rear = None
        self._front = self._front._next
        return popItem

    def peek(self):
        if self.isEmpty():
            raise KeyError("Queue is empty!")
        return self._front._data

    def __iter__(self):
        probe = self._front
        while probe is not None:
            yield probe._data
            probe = probe._next

    def clear(self):
        self._front = None
        self._rear = None


# simple test function
def main():
    ql = QueueLink([7, 4, 0, 500, 400, 600])
    print(ql)
    print(ql.pop())
    print(ql.peek())
    ql.add(4500)
    print(ql)


if __name__ == "__main__":
    ql1 = QueueLink([4, 78, 100, 3, 489])
    ql2 = QueueLink([789, 156, 400, 562])
    ql3 = ql1 + ql2
    print(ql3)
