# 28. Implement strStr()
class SolutionSocheat(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        return haystack.find(needle)


class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0
        ls, lsub = len(haystack), len(needle)
        end = lsub
        while end <= ls:
            if haystack[end-lsub:end] == needle:
                return end-lsub
            end += 1
        return -1
