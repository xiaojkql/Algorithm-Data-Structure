# 383. Ransom Note
import collections


class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        c1 = collections.Counter(ransomNote)
        c2 = collections.Counter(magazine)
        for ch in ransomNote:
            if c1[ch] > c2.get(ch, 0):
                return False
        return True
