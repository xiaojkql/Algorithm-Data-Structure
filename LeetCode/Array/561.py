class Solution:
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        temp = sorted(nums)
        ans = 0
        for i in range(0,len(temp),2):
            ans += temp[i]
        return ans