# -*- coding: utf-8 -*-
'''
Author: Qin Yuan
E-mail: xiaojkql@163.com
Time: 2019-02-16 11:21:51
'''


class Node:
    def __init__(self, data, next=None):  # 外部能直接使用类的数据成员
        self._data = data
        self._next = next

    def data(self):
        return self._data

    def next(self):
        return self._next


if __name__ == "__main__":
    # 使用节点类
    head = None
    for i in range(1, 6):
        head = Node(i, head)
    while head is not None:
        print(head.data())
        head = head.next()
