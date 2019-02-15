# -*- coding: utf-8 -*-
'''
Author: Qin Yuan
E-mail: xiaojkql@163.com
Time: 2019-02-15 21:15:43
'''

"""实际上每一次调整的是每一个序列的第一个元素的位置
找准其位置"""


def quickSort(ls, lo, hi):  # [lo, hi)
    if hi - lo < 2:  # 递归基，单元素就不需要再进行划分
        return
    mi = partition(ls, lo, hi-1)  # 找轴点
    quickSort(ls, lo, mi)  # 对轴点前面的部分进行快排
    quickSort(ls, mi+1, hi)  # 对轴点后面的部分进行快排


def partition(ls, lo, hi):
    pivot = ls[lo]
    while lo < hi:
        while (lo < hi) and (pivot <= ls[hi]):
            hi -= 1
        ls[lo] = ls[hi]
        while (lo < hi) and (ls[lo] <= pivot):
            lo += 1
        ls[hi] = ls[lo]
    ls[lo] = pivot
    return lo


if __name__ == "__main__":
    ls = [4, 5, 7, 2, 4, 6, 2, 4, 10, 11, 1, 0, 3, 9]
    quickSort(ls, 0, len(ls))
    print(ls)
