# -*- coding: utf-8 -*-
'''
Author: Qin Yuan
E-mail: xiaojkql@163.com
Time: 2019-02-16 15:19:55
'''

from node import Node


class DoubleNode(Node):  # 使用继承机制
    def __init__(self, data, prev=None, next=None):
        Node.__init__(self, data, next)  # 使用继承机制
        self._prev = prev

    def previous(self):
        return self._prev


class DoubleLink:
    # 首尾都是哑结点
    def __init__(self):
        self._head = DoubleNode(None)
        self._tail = DoubleNode(None, self._head, None)
        self._head._next = self._tail

    def insertAtFirst(self, value):
        node = DoubleNode(value, self._head, self._head._next)
        self._head._next._prev = node
        self._head._next = node

    def insertAtLast(self, value):
        node = DoubleNode(value, self._tail._prev, self._tail)
        self._tail._prev._next = node
        self._tail._prev = node

    def insertAtIndex(self, index, value):
        if index < 0:
            self.insertAtFirst(value)
        else:
            probe = self._head
            while (index > 0) and (probe._next is not None):
                index -= 1
                probe = probe._next
            node = DoubleNode(value, probe, probe._next)
            probe._next._prev = node
            probe._next = node


if __name__ == "__main__":
    dl = DoubleLink()
    dl.insertAtFirst(100)
    dl.insertAtLast(200)
    dl.insertAtFirst(500)
    dl.insertAtIndex(1, 300)
    print(dl._head._next._data)
    print(dl._head._next._next._data)
    print(dl._head._next._next._next._data)
    print(dl._head._next._next._next._next._data)
