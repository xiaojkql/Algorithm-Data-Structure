import operator,itertools
class Solution:
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        # nums = [val/k for val in nums]
        ans = []
        for i in range(len(nums)-k+1):
            ans.append(sum(nums[i:i+k]))
        return max(ans)

    def findMaxAverageSlidingWindows(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        sums = sum(nums[0:k])
        maxSum = sums
        for i in range(k,len(nums)):
            sums = sums - nums[i-k] + nums[i]
            maxSum = max(sums,maxSum)
        return maxSum/k

    def findMaxAverageMap(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        sums = [0] + list(itertools.accumulate(nums)) # itertool 这个工具的使用
        ans = max(list(map(operator.sub,sums[k:],sums))) # map 函数的使用，将操作逐步映射到各个元素上
        return ans/k