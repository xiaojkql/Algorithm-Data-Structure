# 13. Roman to Integer
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        trans = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100,
                 "D": 500, "M": 1000, "IV": 4, "IX": 9, "XL": 40,
                 "XC": 90, "CD": 400, "CM": 900}
        num = 0
        i = 0
        while i < len(s)-1:
            if s[i] == "I":
                if s[i+1] == "V" or s[i+1] == "X":
                    num += trans[s[i]+s[i+1]]
                    i += 2
                    continue
            if s[i] == "C":
                if s[i+1] == "D" or s[i+1] == "M":
                    num += trans[s[i]+s[i+1]]
                    i += 2
                    continue
            if s[i] == "X":
                if s[i+1] == "L" or s[i+1] == "C":
                    num += trans[s[i]+s[i+1]]
                    i += 2
                    continue
            num += trans[s[i]]
            i += 1
        if i == len(s)-1:
            num += trans[s[len(s)-1]]
        return num


class SolutionJiandShengDeShunxu(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        trans = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000,
                 "IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900}
        num = 0
        for i in range(len(s)-1):
            if trans[s[i]] < trans[s[i+1]]:
                num -= trans[s[i]]
            else:
                num += trans[s[i]]
        num += trans[s[-1]]
        return num
