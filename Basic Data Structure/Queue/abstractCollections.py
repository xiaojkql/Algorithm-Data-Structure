# -*- coding: utf-8 -*-
'''
Author: Qin Yuan
E-mail: xiaojkql@163.com
Time: 2019-02-17 10:14:00
'''

""""底层的数据结构无论是数组还是链表，
在实现队列时都有的函数接口实现"""


class AbstractCollections:

    # 构造元素
    def __init__(self, sourceCollections):
        self._size = 0
        if sourceCollections:
            for item in sourceCollections:
                self.add(item)

    def __len__(self):
        return self._size

    def __str__(self):
        return "{"+",".join(map(str, self))+"}"

    def __add__(self, other):
        result = type(self)(self)
        for item in other:
            result.add(item)

    def __eq__(self, other):
        if self is other:
            return True
        if (type(self) != type(other) or
                len(self) != len(other)):
            return False
        for item in self:
            if item not in other:
                return False
        return True

    def isEmpty(self):
        return self._size == 0
