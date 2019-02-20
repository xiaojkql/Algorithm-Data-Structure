# 551. Student Attendance Record I
class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s.count('A') > 1:
            return False
        if s.find('LLL') != -1:
            return False
        return True

    def checkRecord1(self, s):
        """
        :type s: str
        :rtype: bool
        """
        a = 0
        l = 0
        for ch in s:
            if ch == 'A':
                a += 1
                l = 0
            elif ch == 'L':
                l += 1
            else:
                l = 0
            if l > 2 or a > 1:
                return False
        return True

    def checkRecord2(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return 'LLL' not in s and s.count('A')<2
