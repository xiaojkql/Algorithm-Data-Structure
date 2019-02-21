# 5. Longest Palindromic Substring
# 一个字符串中最长的回文串


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) < 2:
            return s

        ls = [0, 0]

        def search(left, right, ls):
            while 0 <= left and right < len(s) and s[left] == s[right]:
                left, right = left-1, right+1
            if right-left-1 > ls[1]:
                ls[0], ls[1] = left+1, right-left-1

        for i, ch in enumerate(s):

            search(i, i, ls)
            search(i, i+1, ls)

        return s[ls[0]:ls[0]+ls[1]]


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) < 2:
            return s
        start, maxLen = 0, 0
        curr = 0
        while curr < len(s):

            right = left = curr
            # 跳过重复的，noon non 这是一步关键
            while right < len(s)-1 and s[right] == s[right+1]:
                right += 1
            while 0 <= left and right < len(s) and s[left] == s[right]:
                left, right = left-1, right+1
            if maxLen < right-left-1:
                start, maxLen = left+1, right-left-1
            curr += 1
        return s[start:start+maxLen]
