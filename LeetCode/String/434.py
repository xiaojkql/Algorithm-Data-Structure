# 434. Number of Segments in a String
class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans, index = [], 0
        while index < len(s):
            st, count = "", 0
            while index < len(s) and s[index] != " ":
                index, count, st = index+1, count+1, st+s[index]
            if count > 0:
                ans.append(st)
            index += 1
        return len(ans)
