# -*- coding: utf-8 -*-
'''
Author: Qin Yuan
E-mail: xiaojkql@163.com
Time: 2019-02-17 21:48:12
'''

# 二叉搜素树的树节点

import random


class BinNode:
    def __init__(self, data=None, parent=None,
                 lc=None, rc=None, h=0):
        self._data = data
        self._parent = parent
        self._lc = lc
        self._rc = rc
        self._height = h

    # 返回该节点的后代数目
    def size(self):
        s = 1
        # 这里实现的方法隐藏了两个递归
        if self._lc is not None:
            s += self._lc.size()
        if self._rc:
            s += self._rc.size()
        return s

    # 两种插入的方法，作为左孩子或者作为右孩子插入
    def insertAsLc(self, data):
        self._lc = BinNode(data, self)

    def insertAsRc(self, data):
        self._rc = BinNode(data, self)

    # 该节点的直接后继
    def succ(self):
        pass

    # 遍历
    # 先序遍历
    def preTraverse(self):
        # 三个版本：递归，迭代1,2
        def recurse():
            pass

        def iter1():
            pass

        def iter2():
            pass
        sele = random.randint(0, 3)
        if sele == 0:
            recurse()
        elif sele == 1:
            iter1()
        else:
            iter2()

    # 中序遍历

# simple test


def main():
    node1 = BinNode(12)
    node1.insertAsLc(32)
    node1.insertAsRc(666)
    print(node1._lc._data)
    print(node1._rc._data)
    print(node1.size())


if __name__ == "__main__":
    main()
