class Solution:
    def nextGreaterElement(self, nums1: 'List[int]',
                           nums2: 'List[int]') -> 'List[int]':
        d = {}
        st = []
        ans = []
        for num2 in nums2:
            while len(st) and st[-1] < num2:
                d[st.pop()] = num2  # 使用了栈结构
            st.append(num2)
        for num1 in nums1:
            ans.append(d.get(num1, -1))
        return ans
