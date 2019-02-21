# 553. Optimal Division
# 不变的结果


class Solution(object):
    def optimalDivision(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        if len(nums) == 1:
            return "%d" % nums[0]
        if len(nums) == 2:
            return "%d/%d" % (nums[0], nums[1])
        ans = str(nums[0])+"/"+"("+str(nums[1])
        for i in range(2, len(nums)):
            ans += "/" + str(nums[i])
        ans += ")"
        return ans


# 使用了format map
class Solution(object):

    def optimalDivision(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        A = map(str, nums)
        if len(nums) <= 2:
            return "/".join(A)
        return "{}/({})".format(A[0], "/".join(A[1:]))
