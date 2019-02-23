# 202. Happy Number
class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 1:
            return True
        s = set()
        while True:
            if n == 1:
                return True
            ans = 0
            while n:
                ans += (n % 10)**2  # 可以使用sum函数+列表解析化简代码量
                n = n//10
            n = ans
            if n in s:
                return False
            else:
                s.add(n)


class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def squareSum(n):
            ans = 0
            while n:
                ans += (n % 10)**2
                n //= 10
            return ans
        slow = fast = n
        while True:
            slow = squareSum(slow)
            fast = squareSum(fast)
            fast = squareSum(fast)
            if slow == fast:  # 要么一定到达1， # 要么到达另外两个相等的数
                break
        if slow == 1:
            return True
        return False
