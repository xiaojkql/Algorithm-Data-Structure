
class Solution:
    def nextGreaterElements(self, nums: 'List[int]') -> 'List[int]':
        st = []
        ans = [-1]*len(nums)
        print(list(range(len(nums)))*2)
        for i in list(range(len(nums)))*2:
            while st and nums[st[-1]] < nums[i]:
                ans[st.pop()] = nums[i]
            st.append(i)  # 栈中的索引对应的数组值一定是降序的
        return ans
