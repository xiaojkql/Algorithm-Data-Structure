# 859. Buddy Strings
# 在一个str中交换两个字符位置后等于另一个

# 重要的是解决方案的思想


class Solution(object):
    def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if len(A) != len(B):
            return False
        if A == B and len(set(A)) < len(A):
            return True
        diff = [(a, b) for a, b in zip(A, B) if a != b]
        return len(diff) == 2 and diff[0] == diff[-1][::-1]
