# -*- coding: utf-8 -*-
import collections
import heapq
'''
Author: Qin Yuan
E-mail: xiaojkql@163.com
Time: 2019-02-21 23:10:14
'''


# 从可迭代序列中分解出元素
def test1():
    ls = [1, 2, 3]
    a, b, _ = ls
    word = "qin"
    a, b, c = word


# python 中*表达式的应用
def test2():
    ls = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    first, *middle, last = ls
    print(first, middle, last)

    # 或者函数
    def test(a, b):
        print(a, b)
    # 可以这样调用
    arg = [1, 2]
    test(*arg)  # arg可迭代就行


# python yield 的使用 生成一个迭代器，不先返回，而是保存是一个迭代序列
def testYield(x, s):
    for ch in s:
        if ch == x:
            yield ch


def test3():
    x, word = 'q', 'qinqq'
    print(list(testYield(x, word)))


# python collections.deque 保存最近访问的N个元素


# python heapq 的 nlargest,nsmallest 两个函数,堆数据结构的使用
def test4():
    ls = [1, 2, 4, 100, 2, 89, 75, 6]
    print(heapq.nlargest(2, ls))
    print(heapq.nsmallest(2, ls))

    # 有些函数可以接受key从而在更复杂的数据结构上使用该函数，例如sorted，一般key为一个匿名函数，lambda ele:func(elem)
    dic = {"a": 1, "b": 2}
    print(heapq.nlargest(2, dic, key=lambda l: dic[l]))
    heap = list(ls)  # 深度复制
    heapq.heapify(heap)
    heapq.heappop(heap)
    heapq.heappush(heap, 100)


# 字典一对多
def test5():
    dic = collections.defaultdict(list)  # 不需要if key not in dic
    dic[5].append(1)
    print(dic[5])
    dic[5] = dic.get(5, []).append(5)


# 普通字典不会维持元素添加的顺序
# 使用collections.OrderedDict()
# 对字典排序操作时，很可能是在对其key进行操作


if __name__ == "__main__":
    test5()
