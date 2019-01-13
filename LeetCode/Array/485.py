class Solution:
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_local = 0
        max_global = 0
        for num in nums:
            if num == 1:
                max_local += 1
            else:
                max_global = max(max_global, max_local)
                max_local = 0
        return max(max_global, max_local)


    def findMaxConsecutiveOnes_Using_0_1_Structure(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(1, len(nums)):
            if nums[i] == 1:
                nums[i] += nums[i - 1]
            else:
                nums[i] = nums[i]
        return max(nums)