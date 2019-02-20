# 38. Count and Say
class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        # 特征：连续计数
        curr = [1]
        for i in range(n-1):
            next = list()
            say = 1
            j = 0
            while j < len(curr)-1:
                if curr[j] != curr[j+1]:
                    next.append(say)
                    next.append(curr[j])
                    say = 1
                    j += 1
                else:
                    say += 1
                    j += 1
            next.append(say)
            next.append(curr[len(curr)-1])
            curr = next
        return "".join([str(item) for item in curr])


class SolutionOther(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        # 特征：连续计数
        s = "1"
        for _ in range(n-1):
            prev, count, next = s[0], 0, ""
            for curr in s:
                if curr == prev:
                    count += 1
                else:
                    next += str(count) + prev
                    prev = curr
                    count = 1
            next += str(count) + curr
            s = next
        return s
