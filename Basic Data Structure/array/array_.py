# -*- coding: utf-8 -*-
'''
Author: Qin Yuan
E-mail: xiaojkql@163.com
Time: 2019-02-16 10:14:49
'''


class Array:
    """基于python list 实现的一个数组数据结构"""

    def __init__(self, default_capacity=5,
                 logic_size=0, fillValue=None):
        self._elem = list()
        self._default_capacity = default_capacity
        self._capacity = default_capacity
        self._logic_size = logic_size
        self._load_factor = self._logic_size / self._capacity
        for i in range(self._capacity):
            self._elem.append(fillValue)

    def __len__(self):
        return len(self._elem)

    def __str__(self):
        return str(self._elem)

    def __iter__(self):
        return iter(self._elem)

    def __getitem__(self, index):
        return self._elem[index]

    def __setitem__(self, index, value):
        self._elem[index] = value

    def insert(self, index, value):
        for i in range(self._logic_size, index, -1):
            self._elem[i] = self._elem[i-1]
        self._logic_size += 1

    def remove(self, index):
        for i in range(index, self._logic_size-1):
            self._elem[i] = self._elem[i+1]
        self._logic_size -= 1

    def increase(self):
        self.updateLoadFactor()
        if self._load_factor > 0.75:
            temp = [None for _ in range(self._capacity)]
            self._elem += temp
            self._capacity *= 2
        self.updateLoadFactor()

    def shrink(self):
        self.updateLoadFactor()
        if ((self._load_factor < 0.25) and
                (self._capacity//2 > self._default_capacity)):
            temp = self._elem[0:self._capacity//2]
            self._elem = temp
            self._capacity = self._capacity // 2
        self.updateLoadFactor()

    def updateLoadFactor(self):
        self._load_factor = self._logic_size / self._capacity


if __name__ == "__main__":
    arr = Array(10, 10)
    print(arr)
    print(arr[5])
    arr[4] = 100
    print(arr[4])
    a = [_ for _ in arr]
    print(a)
    print(len(arr))
