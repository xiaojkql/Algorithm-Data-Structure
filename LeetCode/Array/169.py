import random
import collections
class Solution:
    def majorityElementSimple(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sorted(nums)[len(nums)//2]

    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        majorityCount = len(nums) // 2
        while True:
            condidate = random.choice(nums)
            if sum(1 for elem in nums if elem == condidate) > majorityCount:
                return condidate

    def majorityElementHashMap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counts = collections.Counter(nums)
        return max(counts.keys(), key=counts.get)  # 前面是一个keys迭代器，返回每一个值，然后传递给counts.get函数获取次数