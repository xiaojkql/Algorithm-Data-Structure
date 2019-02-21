# 125. Valid Palindrome
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        letter = [ch.lower() for ch in s if 'a' <= ch <=
                  'z' or 'A' <= ch <= 'Z' or '0' <= ch <= '9']
        left, right = 0, len(letter)-1
        while left < right:
            if letter[left] != letter[right]:
                return False
            left, right = left+1, right-1
        return True


class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left, right = 0, len(s)-1
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left, right = left+1, right-1
        return True
