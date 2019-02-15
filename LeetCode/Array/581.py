# -*- coding: utf-8 -*-
'''
Author: Qin Yuan
E-mail: xiaojkql@163.com
Time: 2019-02-05 22:30:52
'''


class Solution:
    def findUnsortedSubarray_error(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0 or len(nums) == 1:
            return 0
        if len(nums) == 2:
            if nums[0] > nums[1]:
                return 2
        beg = 0
        end = len(nums) - 1
        for i in range(0, len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] > nums[j]:
                    beg = i
                    break  # 可以使用while语句来写这条满足条件即退出
            if beg != 0:
                break

        for i in range(len(nums)-1, 0, -1):
            for j in range(i-1, -1, -1):
                if nums[i] < nums[j]:
                    end = i
                    break
            if end != len(nums)-1:
                break
        print(beg, end)
        if end == len(nums)-1 and beg == 0:
            return 0
        return end-beg+1 if end >= beg else 0

    def findUnsortedSubarray_sort(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n, sortedNums = len(nums), sorted(nums)
        if nums == sortedNums:
            return 0
        lo = min(i for i in range(n) if nums[i] != sortedNums[i])
        h = max(i for i in range(n-1, -1, -1) if nums[i] != sortedNums[i])
        return h - lo + 1

    def findUnsortedSubarray_advanced(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        is_same = [a == b for a, b in zip(nums, sorted(nums))]
        return 0 if all(is_same) else len(nums)-is_same.index(False) -\
            is_same[::-1].index(False)

    def findUnsortedSubarray_secure(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 保证前面的都比后面小，用前面最大的与后面进行逐步比较，若大于则不符合
        m = nums[0]
        end = 0
        for i in range(1, len(nums)):
            if nums[i] >= m:
                m = nums[i]
            else:
                end = i

        # 保证前面的都比后面小，用后面的最小的与前面的逐步比较
        m = nums[-1]
        start = len(nums)-1
        for i in range(len(nums)-1, -1, -1):
            if nums[i] <= m:
                m = nums[i]
            else:
                start = i

        if start == end:
            return 0

        return max(end-start+1, 0)
