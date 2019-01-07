import collections
class Solution:
    def containsDuplicateSimple(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        numSet = set(nums)
        return (len(numSet) != len(nums))

    def containsDuplicateBruteForce(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # 暴力解法 探究每一个元素
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    return True
        return False

    def containsDuplicateSorted(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # 首先排序
        nums = sorted(nums)
        for i in range(len(nums) - 1):
            if (nums[i] == nums[i + 1]):
                return True
        return False

    def containsDuplicateHash(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        #
        counts = collections.Counter(nums)
        if counts.most_common(1)[0][1]> 1:
            return True
        else:
            return False

if __name__ == "__main__":
    nums = [1,2,2,3,3]
    solution = Solution()
    print(solution.containsDuplicateHash(nums))