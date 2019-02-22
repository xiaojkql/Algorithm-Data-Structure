# 8. String to Integer (atoi)
class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str = str.strip()
        if not str:
            return 0
        sign = False
        if str[0] == "-":
            sign, str = True, str[1:]
        elif str[0] == "+":
            sign, str = False, str[1:]
        ans, mark = "", False
        for ch in str:
            if ch.isdigit():
                if mark:
                    break
                ans += ch
            else:
                mark = True
        if not ans:
            return 0
        ans = -int(ans) if sign else int(ans)
        return -pow(2, 31) if ans < -pow(2, 31) else pow(2, 31)-1 if ans > pow(2, 31)-1 else ans
