# 69. Sqrt(x)
import math


class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        # binary search
        if x <= 1:
            return x
        left, right = 1, x
        while left < right:
            mid = left+(right-left)//2
            if x < mid*mid:
                right = mid
            else:
                left = mid+1
        return right - 1


class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        # binary search
        left, right = 0, x
        while left < right:  # 二分查找关键在于怎样退出
            mid = left+(right-left)//2
            if x < mid*mid:
                right = mid-1
            else:  # mid*mid<=x
                if (mid+1)*(mid+1) > x:  # 说明比mid+1还要大于等于
                    return mid
                left = mid+1
        return right
