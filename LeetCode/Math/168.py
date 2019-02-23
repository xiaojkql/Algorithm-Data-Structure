# 168. Excel Sheet Column Title
class SolutionIte(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return "A"
        ans = ""
        while n > 0:
            n, rest = (n-1)//26, (n-1) % 26
            print(n, rest)
            ans += chr(ord('A')+rest)
        return ans[::-1]


class SolutionRe(object):
    # 很明显的要不断的缩减问题的规模，自然而然的想到了递归解法
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return "A"
        ans = ""
        while n > 0:
            n, rest = (n-1)//26, (n-1) % 26
            print(n, rest)
            ans += chr(ord('A')+rest)
        return ans[::-1]
