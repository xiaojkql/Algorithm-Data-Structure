# -*- coding: utf-8 -*-
'''
Author: Qin Yuan
E-mail: xiaojkql@163.com
Time: 2019-02-15 23:18:22
'''

import random
import time


class Profier:
    def test(self, function, elem=None, size=10, unique=True,
             comp=True, exch=True, trace=True):
        """
        function: 要测试的排序算法函数
        elem: 传递的测试列表
        size: 测试的列表大小
        unique: 是否要求测试的列表中元素独一无二
        comp: 是否记录比较的次数
        exch: 是否记录交换的次数
        trace: 是否在每一次交换后将列表打印出来
        """
        if elem is not None:
            self._elem = elem
        elif unique is True:
            self._elem = list(range(1, size+1))
            random.shuffle(self._elem)
        else:
            self._elem = []
            for i in range(size):
                self._elem.append(random.randint(1, size))
        self._comp = comp
        self._compCount = 0
        self._exch = exch
        self._exchCount = 0
        self._trace = trace
        self.startClock()
        function(self._elem, self)  # 传递的是self本身
        self.stopClock()
        print(self)  # 打印的是self本身, 只需加一个__str__的成员函数即可

    def comparison(self):
        if self._comp is True:
            self._compCount += 1

    def exchange(self):
        if self._exch is True:
            self._exchCount += 1
        if self._trace is True:
            print(self._elem)

    def startClock(self):
        self._start = time.time()

    def stopClock(self):
        self._elapsedTime = round(time.time() - self._start, 3)

    def __str__(self):
        result = "Probelem size:"
        result += (str(len(self._elem))+"\n")
        result += "Elapsed time:"
        result += str(self._elapsedTime) + "\n"
        if self._comp is True:
            result += "Comparison:"
            result += str(self._compCount) + "\n"
        if self._exch is True:
            result += "Exchange:"
            result += str(self._exchCount) + "\n"
        return result
