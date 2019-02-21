# 791. Custom Sort String
class Solution(object):
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        dic = {}
        for i, ch in enumerate(S):
            dic[ch] = i
        for ch in string.lowercase:
            if ch not in dic:
                dic[ch] = len(S)

        def cmp(p, n):
            return -1 if dic[p] < dic[n] else 1
        return "".join(sorted(T, cmp=cmp))


class Solution(object):
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        l = []
        for ch in S:
            if ch in T:
                l.append(ch*T.count(ch))
        for ch in T:
            if ch not in S:
                l.append(ch)
        return "".join(l)
