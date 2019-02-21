# 58. Length of Last Word
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.split()
        if not s:
            return 0
        return len(s[-1])
        # return len(s.rstrip().split(" ")[-1])


class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        tail, ans = len(s)-1, 0
        while tail >= 0 and s[tail] == " ":
            tail -= 1
        while tail >= 0 and s[tail] != " ":
            ans, tail = ans+1, tail-1
        return ans
