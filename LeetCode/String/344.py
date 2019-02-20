# 344. Reverse String
class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: void Do not return anything, modify s in-place instead.
        """
        slen = len(s)
        for i in range(slen//2):
            s[i], s[slen-i-1] = s[slen-i-1], s[i]
        return s[::-1]
