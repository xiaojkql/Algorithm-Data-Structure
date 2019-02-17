# -*- coding: utf-8 -*-
'''
Author: Qin Yuan
E-mail: xiaojkql@163.com
Time: 2019-02-17 18:56:05
'''


class AbstractCollections:
    def __init__(self, sourceCollections):
        self._size = 0
        if sourceCollections:
            for item in sourceCollections:
                self.add(item)

    def __len__(self):
        return self._size

    def __str__(self):
        # 迭代器直接作用于该对象本身上， 因为有迭代器的成员函数
        return "{"+",".join(map(str, self))+"}"

    def __add__(self, other):
        result = type(self)(self)
        for item in other:
            result.add(item)
        return result

    def __eq__(self, other):
        if self is other:
            return True
        if (len(self) != len(other) or
                type(self) != type(other)):
            return False
        for item in self:
            if item not in other:
                return False
        return True

    def isEmpty(self):
        return self._size == 0
