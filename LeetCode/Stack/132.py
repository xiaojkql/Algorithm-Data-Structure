# 132 pattern
class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        st = []
        s3 = -float("inf")
        for num in nums[::-1]:  # 逆序保证了i<j<k
            if num < s3:
                return True
            # 保证了st维护的是一个降序，要么栈顶元素为最大，要么num为最大
            while st and st[-1] < num:
                s3 = st.pop()
            st.append(num)
        return False
