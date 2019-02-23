# 50. Pow(x, n)
class SolutionMyBadRecurse(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        (x, n) = (x, n) if n >= 0 else ((1/x), -n)
        if n == 0:
            return 1
        if n % 2 == 0:
            return self.myPow(x, n//2)*self.myPow(x, n//2)
        else:
            return x*self.myPow(x, n//2)*self.myPow(x, n//2)


class SolutionGoodRecurse(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        (x, n) = (x, n) if n >= 0 else ((1/x), -n)
        if n == 0:
            return 1
        if n % 2 == 0:
            return self.myPow(x, n//2)*self.myPow(x, n//2)
        else:
            return x*self.myPow(x, n//2)*self.myPow(x, n//2)


class SolutionIter(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        (x, n) = (x, n) if n >= 0 else ((1/x), -n)
        ans, p = 1, x
        while n > 0:
            if n % 2 == 0:
                p *= p
                n = n//2
            else:
                ans *= p  # 包含了1
                n = n-1
        return ans


class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        (x, n) = (x, n) if n >= 0 else ((1/x), -n)
        ans, p = 1, x
        while n > 0:
            if n % 2 & 1:
                ans *= p  # 包含了1
            p *= p
            n >>= 1
        return ans
