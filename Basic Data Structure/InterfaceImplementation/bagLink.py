# -*- coding: utf-8 -*-
'''
Author: Qin Yuan
E-mail: xiaojkql@163.com
Time: 2019-02-16 19:10:14
'''

from LinkedStructure.node import Node


class BagLink:
    """Interface for all bag type"""

    # constructor
    def __init__(self, sourceCollections=None):
        """Sets the initial states of self, which includes the
        contents of sourceCollections, if it's present."""
        self._items = None  # 没有哑结点
        self._size = 0
        if sourceCollections:
            for item in sourceCollections:
                self.add(item)

    # Accessor method
    def isEmpty(self):
        """Return True if len(self)==0,
        False otherwise"""
        return self._size == 0

    def __len__(self):
        """Return the number of items in bag"""
        return self._size

    def __str__(self):
        """Return the string representation of self"""
        return "{"+",".join(map(str, self))+"}"

    def __iter__(self):
        """Supports iteration over a view of self."""
        cursor = self._items  # 没有哑结点，head本身就表示第一个元素
        while cursor:
            yield cursor._data
            cursor = cursor._next

    def __add__(self, other):
        """Return a new bag containing the contents of self and other"""
        result = BagLink(self)
        for item in other:
            result.add(item)
        return result

    def __eq__(self, other):
        """Return True if self equals other"""
        if self is other:
            return True
        if type(self) is not type(other) or\
                len(self) != len(other):
            return False
        for item in self:
            if item not in other:
                return False
        return True

    # Mutator methods

    def clear(self):
        """Make self empty"""
        self._size = 0
        self._items = None

    def add(self, item):
        """Adds item to self"""
        self._items = Node(item, self._items)
        self._size += 1

    def remove(self, item):
        """
        precondition: item is in self.
        Raise: KeyError if item in not in self
        Postcondition: item is removed from self.
        """
        if item not in self:
            raise KeyError(str(item)+" not in bag.")
        probe = self._items
        prev = None
        for target in self:
            if target == item:
                break
            prev = probe
            probe = probe._next
        if probe is self._items:
            self._items = self._items._next
        else:
            prev._next = probe._next
        self._size -= 1
