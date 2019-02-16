# -*- coding: utf-8 -*-
'''
Author: Qin Yuan
E-mail: xiaojkql@163.com
Time: 2019-02-16 16:19:47
'''

from arrays import Array


class BagArray:
    """Interface for all bag type"""

    # class variable
    DEFULAT_CAPACITY = 10

    # constructor
    def __init__(self, sourceCollections=None):
        """Sets the initial states of self, which includes the
        contents of sourceCollections, if it's present."""
        self._item = Array(BagArray.DEFULAT_CAPACITY)
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

    def __iter__(self):
        """Supports iteration over a view of self."""
        cursor = 0
        while cursor < self._size:
            yield self._item[cursor]  # 使用yield语句
            cursor += 1

    def __add__(self, other):
        """Return a new bag containing the contents of self and other"""
        result = BagArray(self)
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

    # Mutator methods

    def clear(self):
        """Make self empty"""
        self._size = 0
        self._item = Array(BagArray.DEFULAT_CAPACITY)

    def add(self, item):
        """Adds item to self"""
        self._item[len(self)] = item
        self._size += 1

    def remove(self, item):
        """
        precondition: item is in self.
        Raise: KeyError if item in not in self
        Postcondition: item is removed from self.
        """
        # 检查先验条件
        if not (item in self):
            raise KeyError(str(item)+"not in bag")
        # 查找item的位置
        itemIndex = 0
        for target in self:
            if target == item:
                break
            itemIndex += 1
        # 向前移动元素
        for i in range(itemIndex, len(self)):
            self._item[i] = self._item[i+1]
        # 将size缩减1
        self._size -= 1
