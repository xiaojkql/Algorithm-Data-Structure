# -*- coding: utf-8 -*-
'''
Author: Qin Yuan
E-mail: xiaojkql@163.com
Time: 2019-01-22 15:49:29
'''


def lineSearch(ls, target):
    """用线性搜索方法在列表中查找目标元素target，
    若找到则返回其index,否则返回-1"""
    if not ls:
        return -1
    for i in range(len(ls)):
        if ls[i] == target:
            return i
    return -1


if __name__ == "__main__":
    ls = [0, 1, 4, 5, 2, 8, 2, 6, 54, 1, 2, 5, 100]
    print(lineSearch(ls, 100))
    print(lineSearch(ls, 200))
