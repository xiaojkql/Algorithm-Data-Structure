# 788. Rotated Digits
class Solution(object):
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        count = 0
        for i in range(1, N+1):
            num = str(i)
            if '3' in num or '7' in num or '4' in num:
                continue
            if '2' in num or '5' in num or '6' in num or '9' in num:
                count += 1
        return count
