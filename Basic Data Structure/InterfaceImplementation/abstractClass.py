# -*- coding: utf-8 -*-
'''
Author: Qin Yuan
E-mail: xiaojkql@163.com
Time: 2019-02-16 16:19:47
'''


class AbstractBag:
    """Interface for all bag type"""

    # constructor
    def __init__(self, sourceCollections=None):
        """Sets the initial states of self, which includes the
        contents of sourceCollections, if it's present."""
        self._size = 0  # 记录该包中的数据项的逻辑大小
        if sourceCollections:
            for item in sourceCollections:
                self.add(item)

    # Accessor method
    def isEmpty(self):
        """Return True if len(self)==0,
        False otherwise"""
        return len(self) == 0

    def __len__(self):
        """Return the number of items in bag"""
        return self._size

    def __str__(self):
        """Return the string representation of self"""
        return "{"+",".join(map(str, self))+"}"  # 使用join方法，以及使用map函数，使用str函数

    def __add__(self, other):
        """Return a new bag containing the contents of self and other"""
        result = type(self)(self)
        for item in other:
            result.add(item)
        return result

    def __eq__(self, other):
        """Return True if self equals other"""
        if self is other:
            return True
        if type(self) != type(other) or\
                len(self) != len(other):
            return False
        for item in self:
            if not (item in other):
                return False
        return True
