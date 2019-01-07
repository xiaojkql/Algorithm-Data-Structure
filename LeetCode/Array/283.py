class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # just relying on sort implementation
        # nums.sort(key=lambda x:1 if x == 0 else 0)
        nums.sort(key=bool, reverse=True)

    def moveZeroes1(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # brute Force
        ans = []
        count = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                count += 1
            else:
                ans.append(nums[i])
        nums[:] = [0 for i in range(count)]
        nums[:] = ans[:] + nums[:]

    def moveZeroes2(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        nonZero = 0
        countZero = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                countZero += 1
            else:
                nums[nonZero] = nums[i]
                nonZero += 1
        for i in range(countZero):
            nums[nonZero + i] = 0

    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        lastZero = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                temp = nums[lastZero]
                nums[lastZero] = nums[i]
                nums[i] = temp
                lastZero += 1