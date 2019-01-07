class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        unique_trail = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[unique_trail]:
                unique_trail += 1
                nums[unique_trail] = nums[i]
        return unique_trail + 1

if __name__ == "__main__":
    solution = Solution()
    nums = [1,2,2,3,3,4,5,5,6,7,7,8,8]
    print(solution.removeDuplicates(nums))
    print(nums)