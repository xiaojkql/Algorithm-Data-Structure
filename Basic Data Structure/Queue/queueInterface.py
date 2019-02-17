# -*- coding: utf-8 -*-
'''
Author: Qin Yuan
E-mail: xiaojkql@163.com
Time: 2019-02-17 10:07:02
'''

"""The inerface of queue"""


class QueueInterface:

    # constructor
    def __init__(self, sourceCollections):
        pass

    # mutator method

    # 向队尾添加元素
    def add(self, item):
        pass

    # 弹出队头的元素
    def pop(self):
        pass

    # 查看队头元素
    def peek(self):
        pass

    # len
    def __len__(self):
        return 0

    # str
    def __str__(self):
        return ""

    # eq
    def __eq__(self):
        return True

    # +运算符
    def __add__(self):
        return 0

    # iter 迭代器
    def __iter__(self):
        return 0
