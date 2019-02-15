# -*- coding: utf-8 -*-
'''
Author: Qin Yuan
E-mail: xiaojkql@163.com
Time: 2019-01-15 18:38:54
'''

# 两种实现方式都是稳定的，可以保持相等元素的输入顺序性
# 最好情况就是已经排序好了只需n-1次比较，复杂度为O(n)
# 最坏情况就是完全逆序，0,1,2,...,n 次交换，比较，复杂度为O(n^2)
# 使用的策略为减而治之


class BubbleSort():
    def version1(self, nums, lo, hi):  # [lo, hi)
        sorted = False
        for i in range(hi, lo, -1):  # 不包含第一项
            if sorted is True:
                break
            sorted = True
            # 从第二项开始
            for j in range(lo+1, i):  # 不包含比较的最后一项
                if nums[j-1] > nums[j]:
                    nums[j], nums[j-1] = nums[j-1], nums[j]
                    sorted = False

    def version2(self, nums, lo, hi):  # [lo,hi),对于后面已经排好序的就不必要再检查了
        while lo < hi:
            last = lo
            for i in range(lo+1, hi):
                if nums[i-1] > nums[i]:
                    nums[i-1], nums[i] = nums[i], nums[i-1]
                    last = i  # 已经默认了不包含此元素的
            hi = last


if __name__ == "__main__":
    sort = BubbleSort()
    nums = [5, 4, 6, 75, 23, 5, 6, 1, 2, 3, 100]
    sort.version2(nums, 0, 5)
    print(nums)
