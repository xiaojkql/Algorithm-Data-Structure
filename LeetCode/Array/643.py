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