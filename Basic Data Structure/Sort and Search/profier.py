# -*- coding: utf-8 -*-
'''
Author: Qin Yuan
E-mail: xiaojkql@163.com
Time: 2019-02-15 23:18:22
'''


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
