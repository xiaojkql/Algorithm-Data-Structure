class Solution:
    def missingNumberBruteforce(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        for i in range(n+1):
            if i not in nums:
                return i

    def missingNumberHashSet(self, nums):  # This is accepted O(n)
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        setNums = set(nums)
        for i in range(n + 1):
            if i not in setNums:
                return i


    def missingNumberSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 用求和差
        expectSum = len(nums) * (len(nums) + 1) // 2
        realSum = sum(nums)  # O(n)
        return expectSum - realSum

    def missingNumberXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        missing = len(nums)
        for i in range(len(nums)):
            missing ^= i ^ nums[i]
        return missing

    def missingNumberSorted(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 用排序后进行检查 因为是[0,...,n]
        # 还有特殊情况存在
        if not nums:
            return 0
        nums = sorted(nums)
        for i in range(len(nums)):
            if i != nums[i]:
                return i
        return len(nums)