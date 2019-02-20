# 459. Repeated Substring Pattern
class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        sub = ""
        for ch in s:
            sub += ch
            sLen, subLen = len(s), len(sub)
            if subLen > sLen // 2:
                return False
            if sLen % subLen == 0:
                if sub*(sLen//subLen) == s:
                    return True


class SolutionBrilliant(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return False
        str = (s + s)[1:-1]
        return str.find(s) != -1
