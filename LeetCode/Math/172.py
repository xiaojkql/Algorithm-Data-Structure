# 172. Factorial Trailing Zeroes
class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = 1
        while n > 1:
            ans, n = ans*n, n-1
        count = 0
        for ch in str(ans)[::-1]:
            if ch == "0":
                count += 1
            else:
                break
        return count


class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = 0
        five = 5
        while True:
            inte = n//five
            if inte == 0:
                return ans
            ans += inte
            five *= 5


class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        return 0 if n == 0 else n/5 + self.trailingZeroes(n/5)
