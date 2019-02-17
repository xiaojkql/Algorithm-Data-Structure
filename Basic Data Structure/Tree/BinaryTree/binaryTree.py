# -*- coding: utf-8 -*-
'''
Author: Qin Yuan
E-mail: xiaojkql@163.com
Time: 2019-02-17 22:17:48
'''

from binNode import BinNode


class BinaryTree:
    def __init__(self):
        self._size = 0
        self._root = BinNode()

    def size(self):
        return self._size
    
    def isEmpty(self):
        return self._size == 0
    
    def root(self):
        return self._root
