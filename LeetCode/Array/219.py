class Solution:
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        dict = {}
        for i in range(len(nums)): # 或者用i,v in enumerate(nums)
            if nums[i] in dict and i-dict[nums[i]]<=k:
                return True
            else:
                dict[nums[i]] = i
        return False