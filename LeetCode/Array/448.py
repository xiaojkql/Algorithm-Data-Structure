class Solution:
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        setNums = set(nums)
        ans = []
        for i in range(len(nums)):
            i += 1
            if i not in setNums:
                ans.append(i)
        return ans

    def findDisappearedNumbersSet(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return list(set(range(1, len(nums) + 1)).difference(set(nums)))
        # set(A) - set(B) 集合之间的运算


    def findDisappearedNumbers_Mannual(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in range(len(nums)):
            index = abs(nums[i]) - 1
            nums[index] = -abs(nums[index])
        return [i + 1 for i in range(len(nums)) if nums[i] > 0]