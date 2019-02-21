# 647. Palindromic Substrings
# 计数字符串中回文串的个数


class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 写迭代的
        count, curr = 0, 0
        while curr < len(s):
            left = right = curr
            while right < len(s)-1 and s[right] == s[right+1]:
                count, right = count+1, right+1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left, right, count = left-1, right+1, count+1
            curr += 1
        return count
