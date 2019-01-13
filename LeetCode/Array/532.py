import collections


class Solution:
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k > 0:
            return len(set(nums) & set([v+k for v in nums]))
        if k < 0:
            return 0
        return sum(v > 1 for v in collections.Counter(nums).values())

    def findPairs_oneline(self, nums, k):
        return (len(set(nums) & set([v+k for v in nums])) if k > 0
                else sum(v > 1 for v in collections.Counter(nums).values()) if k == 0
                else 0)
