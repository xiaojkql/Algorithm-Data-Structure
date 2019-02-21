# 14. Longest Common Prefix
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        ans, short = "", min([len(str1) for str1 in strs])
        for i in range(short):
            ans += strs[0][i]
            for str1 in strs:
                if ans != str1[0:i+1]:
                    return ans[:-1]
        return ans


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        sMin, sMax = min(strs), max(strs)
        for i, ch in enumerate(sMin):
            if ch != sMax[i]:
                return sMin[:i]
        return sMin


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        for i, item in enumerate(zip(*strs)):
            if len(set(item)) > 1:
                return strs[0][:i]
        return min(strs)
