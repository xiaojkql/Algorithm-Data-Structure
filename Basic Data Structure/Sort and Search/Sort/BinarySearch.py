# -*- coding: utf-8 -*-
'''
Author: Qin Yuan
E-mail: xiaojkql@163.com
Time: 2019-01-15 20:37:31
'''

# 二分查找，策略是减而治之
# 注意此算法是针对有序的数组，向量的


class BinarySearch():
    def version1(self, val, nums, lo, hi):  # 三个判断，最好的情况能提前退出，即nums[mid] == e时
        while(lo < hi):  # 能查找完毕，因为[lo, hi) 的一半 mid = lo 已经检查了
            mid = (lo + hi)//2  # [lo,hi) mid = lo所以就已经检查完毕
            if nums[mid] == val:
                return mid
            elif nums[mid] > val:
                hi = mid
            else:
                lo = mid + 1
        return -1

    # 保证 nums[lo] <= val 若要保证次序，则可以lo+1
    # 若要保证插入后保持次序，则
    def version2(self, val, nums, lo, hi):
        while(hi-lo > 1):  # 最后剩一个元素，[lo, hi) 保证了nums[lo]<=val，所以要么在里面要么就不在里面
            mid = (lo + hi)//2  # 保证了所有index都在序列之中
            if nums[mid] <= val:
                lo = mid  # 使 lo始终在包含val的index之中
            else:
                hi = mid  # 使 hi始终不在包含val的index之中
        return lo+1

    # nums[hi-1]>=val>nums[lo] lo+1要么大于，要么等于
    # 最后剩[lo,hi)
    def version3(self, val, nums, lo, hi):
        while(hi-lo > 1):
            mid = (lo + hi)//2
            if nums[mid] >= val:
                hi = mid
            else:
                lo = mid
        return lo+1

    def version4(self, val, nums, lo, hi):
        while(hi-lo > 1):
            mid = (lo + hi)//2
            if nums[mid] > val:
                hi = mid
            else:
                lo = mid
        return lo if nums[lo] == val else -1


if __name__ == "__main__":
    nums = [1, 2, 5, 8, 9, 10, 11, 12, 13]
    search = BinarySearch()
    val = 10
    print(search.version4(val, nums, 0, len(nums)))
    print(nums)


