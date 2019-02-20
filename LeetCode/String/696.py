# 696. Count Binary Substrings
class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s or len(s) == 1:
            return 0
        ans = [1]
        curr = 0
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                ans[curr] += 1
            else:
                ans.append(1)
                curr += 1
        num = 0
        # for i in range(1,len(ans)):
        #    num += min(ans[i-1],ans[i])
        # num = sum(min(ans[i-1],ans[i]) for i in range(1,len(ans)))
        # 使用zip
        num = sum(min(a, b) for a, b in zip(ans, ans[1:]))
        return num


class SolutionConcise(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = map(len, s.replace('01', '0 1').replace('10', '1 0').split(' '))
        num = sum(min(a, b) for a, b in zip(ans, ans[1:]))
        return num
