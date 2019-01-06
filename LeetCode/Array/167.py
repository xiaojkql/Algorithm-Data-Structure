class Solution:
    def twoSumComplex(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not numbers:
            return[0,0]
        tempDict = {}
        tempDict[numbers[0]] = 0
        for i in range(1,len(numbers)):
            if target-numbers[i] not in tempDict:
                tempDict[numbers[i]] = i
            else:
                return [tempDict[target-numbers[i]]+1,i+1]

    def twoSumTwoPointer(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not numbers or len(numbers) == 1:
            return [0, 0]

        lo, hi = 0, len(numbers) - 1
        while (lo < hi):
            s = numbers[lo] + numbers[hi]
            if s == target:
                return [lo + 1, hi + 1]
            elif s < target:
                lo += 1
            else:
                hi -= 1
        return [0, 0]

    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not numbers or len(numbers) == 1:
            return [0, 0]

        lo, hi = 0, len(numbers) - 1
        s = numbers[lo] + numbers[hi]
        while ((s) != target):
            if s < target:
                lo += 1
            else:
                hi -= 1
            s = numbers[lo] + numbers[hi]
        return [lo + 1, hi + 1]