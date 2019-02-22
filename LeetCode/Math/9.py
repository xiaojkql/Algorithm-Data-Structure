# 9. Palindrome Number
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        x = str(x)
        left, right = 0, len(x)-1
        while left < right:
            if x[left] != x[right]:
                return False
            left, right = left+1, right-1
        return True


class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x = str(x)
        return x == x[::-1]


class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        ans, oRx = 0, x
        while oRx:
            ans, oRx = ans*10+oRx % 10, oRx//10  # 构建新得数
        print(ans)
        return ans == x
