class Solution:
    def thirdMaxPyrhonBuiltInMethod(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        setNums = list(set(nums))
        setNums.sort()
        if len(setNums) < 3:
            return setNums[-1]
        else:
            return setNums[-3]

    class Solution:
        def thirdMax(self, nums):
            """
            :type nums: List[int]
            :rtype: int
            """
            high = middle = low = -float("inf")
            for num in nums:
                if num in (high, middle, low): continue
                if num > high: high, num = num, high
                if num > middle: middle, num = num, middle
                if num > low: low, num = num, low
            return high if low == -float("inf") else low