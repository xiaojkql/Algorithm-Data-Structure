import itertools
import numpy as np


class Solution:
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        if len(nums)*len(nums[0]) != r*c:
            return nums
        # 使用列表解析，里面包含两个for循环
        ans = [[None]*c for _ in range(r)]
        ls = [val for row in nums for val in row]
        ls = sum(nums, [])
        for i in range(r):
            for j in range(c):
                ans[i][j] = ls[i*c+j]
        return ans

    def matrixReshape_ite(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        if len(nums)*len(nums[0]) != r*c:
            return nums
        # 使用列表解析，里面包含两个for循环
        nums = itertools.chain(*nums)
        ans = [[next(nums) for i in range(c)] for j in range(r)]
        ans = [list(itertools.islice(nums, c)) for _ in range(r)]
        return ans
    def matrixReshapeNumpy(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        if len(nums)*len(nums[0]) != r*c:
            return nums
        ans = np.reshape(nums,(r,c)).tolist()
        return ans
