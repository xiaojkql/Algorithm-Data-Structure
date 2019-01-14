class Solution:
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        ans1 = nums[0] * nums[1] * nums[-1]
        ans2 = nums[-1] * nums[-2] * nums[-3]
        return ans1 if ans1 > ans2 else ans2