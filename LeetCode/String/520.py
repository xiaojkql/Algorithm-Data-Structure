# 520. Detect Capital
class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if word.islower() or word.isupper():
            return True
        if word[0].islower():
            return False
        if word[1:].islower():
            return True
        return False
