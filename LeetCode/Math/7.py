# 7. Reverse Integer
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        print(x > 2**31)
        if x < -(2**31) or x > (2**31-1):
            return 0
        f = True if x < 0 else False
        s = str(abs(x))[::-1].rstrip("0")
        if int(s) < -(2**31) or int(s) > (2**31-1):
            return 0
        return -int(s) if f else int(s)


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = False
        if x < 0:
            sign = True
        res, x = 0, abs(x)
        while x:
            res, x = res*10 + x % 10, x//10  # 逆转数字的方法
        if sign:
            res = -res
        return res if -pow(2, 31) <= res <= pow(2, 31)-1 else 0
