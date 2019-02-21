# 至多删除一个字符后是否是回文
class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left, right = 0, len(s)-1
        while left < right:
            if s[left] != s[right]:
                sl, sr = s[left:right], s[left+1:right+1]
                return sl == sl[::-1] or sr == sr[::-1]
            left, right = left+1, right-1
        return True
