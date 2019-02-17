# -*- coding: utf-8 -*-
'''
Author: Qin Yuan
E-mail: xiaojkql@163.com
Time: 2019-02-17 19:32:38
'''


class ListArrayIter:
    def __init__(self, backStore):
        self._modCount = backStore.getModCount()
        self._backStore = backStore  # 表示一个列表对象实例
        self.first()  # 初始化时，游标设置处于首位置

    def first(self):
        self._cursor = 0  # 游标实例变量
        self._itemPos = -1  # 当前指向元素的位置

    def hasNext(self):
        return self._cursor < len(self._backStore)

    def next(self):
        if not self.hasNext():
            raise ValueError("not have next item in list")
        if self._modCount != self._backStore.getModCount():
            raise AttributeError("Illegal modification")
        self._itemPos = self._cursor
        self._cursor += 1
        return self._backStore[self._itemPos]

    def last(self):
        self._cursor = len(self._backStore)

    def hasPrevious(self):
        return self._cursor > 0

    def previous(self):
        if not self.hasPrevious():
            raise ValueError("not have previous item in list")
        if self._modCount != self._backStore.getModCount():
            raise AttributeError("Illegal modification")
        self._cursor -= 1
        self._itemPos = self._cursor
        return self._backStore[self._itemPos]

    def replace(self, item):
        if self._itemPos == -1:
            raise AttributeError("The current postion is undefined")
        if self._modCount != self._backStore.getModCount():
            raise AttributeError("Illegal replace")
        self._backStore[self._itemPos] = item
        self._itemPos = -1

    def insert(self, item):
        if self._modCount != self._backStore.getModCount():
            raise AttributeError("Illegal insert")
        if self._itemPos == -1:
            self._backStore.add(item)
        else:
            self._backStore.insert(self._itemPos, item)
        self._itemPos = -1
        self._modCount += 1

    def remove(self):
        if self._itemPos == -1:
            raise AttributeError("Undefined")
        if self._modCount != self._backStore.getModCount():
            raise AttributeError("Illegal remove")
        self._backStore.pop(self._itemPos)
        if self._cursor > self._itemPos:
            self._cursor -= 1
        self._modCount += 1
        self._itemPos = -1
