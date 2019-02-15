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
    mi = partitionB(ls, lo, hi-1)  # 找轴点
    quickSort(ls, lo, mi)  # 对轴点前面的部分进行快排
    quickSort(ls, mi+1, hi)  # 对轴点后面的部分进行快排


def partitionA(ls, lo, hi):  # 对区间[lo, hi]区间中的列表元素进行划分
    """此版本是将小于等于候选pivot归入左边
    大于等于候选pivot的归入右边"""
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


def partitionB(ls, lo, hi):  # 对[lo, hi]区间中的列表元素进行划分
    """此版本是将大于候选pivot的归入右边
    将小于候选pivot的归入左边"""
    pivot = ls[lo]  # 将首元素作为候选轴点
    while lo < hi:
        while lo < hi:
            if pivot < ls[hi]:
                hi -= 1
            else:
                ls[lo] = ls[hi]
                lo += 1
                break
        while lo < hi:
            if ls[lo] < pivot:
                lo += 1
            else:
                ls[hi] = ls[lo]
                hi -= 1
                break
    ls[lo] = pivot
    return lo


if __name__ == "__main__":
    ls = [4, 5, 7, 2, 4, 6, 2, 4, 10, 11, 1, 0, 3, 9]
    quickSort(ls, 0, len(ls))
    print(ls)
