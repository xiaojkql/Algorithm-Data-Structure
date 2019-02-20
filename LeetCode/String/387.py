# 387. First Unique Character in a String
import collections


class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        countS = collections.Counter(s)
        single = [ch for ch, i in countS.items() if i == 1]
        print(single)
        if not single:
            return -1
        for i in range(len(s)):
            if s[i] in single:
                return i

    def firstUniqChar2(self, s):
        """
        :type s: str
        :rtype: int
        """
        for ch in s:
            if s.count(ch) == 1:
                return s.index(ch)
        return -1
