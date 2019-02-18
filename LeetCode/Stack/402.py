# 402. Remove K Digits


class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        # 使用贪心策略，首先从高位移走
        st = []

        for ch in num:
            while st and int(ch) < int(st[-1]) and k > 0:
                st.pop()
                k -= 1
            st.append(ch)

        # 一种特殊情况
        while k > 0:
            st.pop()
            k -= 1

        digit = "".join(st).lstrip("0")

        return digit if digit else "0"  # 当为空时就是False 不能比较
