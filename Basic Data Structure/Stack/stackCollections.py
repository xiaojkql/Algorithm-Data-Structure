# -*- coding: utf-8 -*-
'''
Author: Qin Yuan
E-mail: xiaojkql@163.com
Time: 2019-02-16 21:46:34
'''


class StackCollections:
    def __init__(self, sourceCollections):
        self._size = 0
        if sourceCollections:
            for item in sourceCollections:
                self.add(item)

    def size(self):
        return self._size

    def isEmpty(self):
        return self.size() == 0

    def __len__(self):
        return self.size()

    def __add__(self, other):
        result = type(self)(self)
        for item in other:
            result.add(item)
        return result

    def __str__(self):
        return "{"+",".join(map(str, self))+"}"

    def __eq__(self, other):
        if self is other:
            return True
        if (type(self) != type(other) or
                self.size() != self.size()):
            return False
        for item in self:
            if item not in other:
                return False
        return True
