# 29. Divide Two Integers
class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        # 除法就是减法
        sign = (dividend < 0) is (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
        ans = 0
        while dividend >= divisor:
            dividend, ans = dividend-divisor, ans+1
        if not sign:
            ans = -ans
        return min(max(-pow(2, 31), ans), pow(2, 31)-1)


class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        # 除法就是减法
        sign = (dividend < 0) is (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
        ans = 0
        while dividend >= divisor:  # 一个循环太慢了
            tmp, i = divisor, 1
            while dividend >= tmp:
                dividend -= tmp
                ans += i
                i <<= 1
                tmp <<= 1

        if not sign:
            ans = -ans
        return min(max(-pow(2, 31), ans), pow(2, 31)-1)
