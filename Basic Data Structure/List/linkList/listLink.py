# -*- coding: utf-8 -*-
'''
Author: Qin Yuan
E-mail: xiaojkql@163.com
Time: 2019-02-17 20:29:39
'''

from abstractList import AbstractList
from doubleLink import DoubleNode


# 设置一个_head空的头节点
class ListLink(AbstractList):
    def __init__(self, sourceCollections=None):
        self._head
