# -*- coding: utf-8 -*-
'''
Author: Qin Yuan
E-mail: xiaojkql@163.com
Time: 2019-01-22 16:12:09
'''


class Consumer:
    def __init__(self, name, wage):
        self._name = name
        self._wage = wage

    def __lt__(self, other):
        return self._wage < other._wage

    def __le__(self, other):
        return self._wage <= other._wage

    def __gt__(self, other):
        return self._wage > other._wage

    def __ge__(self, other):
        return self._wage >= other._wage

    def __eq__(self, other):
        return self._wage == other._wage


if __name__ == "__main__":
    C1 = Consumer("QY", 100)
    C2 = Consumer("JCZ", 200)
    print(C1 < C2)
    print(C1 == C2)
    print(C1 > C2)
    print(C1 <= C2)
    print(C1 >= C2)
