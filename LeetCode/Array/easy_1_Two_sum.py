class Solution:
    def twoSum(self,nums,target):
        """

        :param nums: list[int]
        :param target: int
        :return: list[int]
        """
        temp_dict = {}
        for i in range(len(nums)):
            dif = target-nums[i]
            if dif not  in temp_dict:
                temp_dict[nums[i]] = i
            else:
                return [temp_dict[dif],i]

if __name__ == "__main__":
    nums = [4,5,7,8,9,10]
    solution = Solution()
    print(solution.twoSum(nums,18))