# 171. Excel Sheet Column Number
import functools


class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = ord(s[0])-ord('A')+1
        for ch in s[1:]:
            ans = ans*26+ord(ch)-ord('A')+1
        return ans


class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 使用了reduce
        ans = functools.reduce(lambda x, y: x*26+(ord(y)-ord('A')+1), s, 0)
        return ans
