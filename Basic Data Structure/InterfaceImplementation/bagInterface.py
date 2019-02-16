# -*- coding: utf-8 -*-
'''
Author: Qin Yuan
E-mail: xiaojkql@163.com
Time: 2019-02-16 16:19:47
'''


class Bag:
    """Interface for all bag type"""

    # constructor
    def __init__(self, sourceCollections=None):
        """Sets the initial states of self, which includes the
        contents of sourceCollections, if it's present."""
        pass

    # Accessor method
    def isEmpty(self):
        """Return True if len(self)==0,
        False otherwise"""
        return True

    def __len__(self):
        """Return the number of items in bag"""
        return 0

    def __str__(self):
        """Return the string representation of self"""
        return ""

    def __iter__(self):
        """Supports iteration over a view of self."""
        return None

    def __add__(self, other):
        """Return a new bag containing the contents of self and other"""
        return None

    def __eq__(self, other):
        """Return True if self equals other"""
        return False

    # Mutator methods
    def clear(self):
        """Make self empty"""
        pass

    def add(self, item):
        """Adds item to self"""
        pass

    def remove(self, item):
        """
        precondition: item is in self.
        Raise: KeyError if item in not in self
        Postcondition: item is removed from self.
        """
        pass
