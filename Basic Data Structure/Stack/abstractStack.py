# -*- coding: utf-8 -*-
'''
Author: Qin Yuan
E-mail: xiaojkql@163.com
Time: 2019-02-16 21:57:30
'''

from stackCollections import StackCollections


class AbstractStack(StackCollections):
    def __init__(self, sourceCollections):
        StackCollections.__init__(self, sourceCollections)

    def add(self, item):
        self.push(item)
