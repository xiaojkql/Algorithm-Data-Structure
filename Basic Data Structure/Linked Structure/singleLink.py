# -*- coding: utf-8 -*-
'''
Author: Qin Yuan
E-mail: xiaojkql@163.com
Time: 2019-02-16 11:29:26
'''

from node import Node


class SingleLink:
    def __init__(self):
        self._head = None

    def head(self):  # 获取头节点
        return self._head

    def insertAsFirst(self, value):
        self._head = Node(value, self._head)
        # 单链表的头结点始终是指向第一个元素的，且每次从头部向列表中插入元素时，都是插入到第一个节点处

    def deleFirst(self):
        data = self._head._data
        self._head = self._head._next
        return data

    def insertAsLast(self, value):
        newNode = Node(value)
        if self._head is None:
            self._head = newNode
        else:
            temp = self._head
            while temp._next is not None:
                temp = temp._next
            temp._next = newNode

    def deleLast(self):
        # 两种情况只有一个元素，以及有多个元素
        if self._head._next is None:
            self._head = None
        else:
            probe = self._head
            while (probe._next._next is not None):
                probe = probe._next
            removeData = probe._next._data
            probe._next = None
            return removeData

    def insert(self, node, value):
        pass

    def traverse(self, function):
        probe = self._head
        while probe is not None:
            function(probe._data)
            probe = probe._next

    def search(self, target_value):
        probe = self._head
        while ((probe is not None) and
               (probe._data != target_value)):
            probe = probe._next
        return True if probe is not None else False

    def __getitem__(self, index):
        probe = self._head
        while ((index != 0) and (probe is not None)):
            probe = probe._next
        return probe._data

    def replace(self, oldValue, newValue):
        probe = self._head
        while ((probe is not None)
               and (probe._data != oldValue)):
            probe = probe._next
        if probe is not None:
            probe._data = newValue
            return True
        else:
            return False
