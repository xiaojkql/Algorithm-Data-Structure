# 345. Reverse Vowels of a String
class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = "aeiouAEIOU"
        st = list(filter(lambda l: l in vowels, s))
        return "".join([st.pop() if ch in vowels else ch for ch in s])


class SolutionTwopointers(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Two pointers method
        vowels = set("aeiouAEIOU")
        s = list(s)  # 一定要换成list
        l, r = 0, len(s)-1
        while l <= r:
            if s[l] in vowels and s[r] in vowels:
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1
            elif s[l] in vowels and s[r] not in vowels:
                r -= 1
            elif s[l] not in vowels and s[r] in vowels:
                l += 1
            else:
                l += 1
                r -= 1
        return "".join(s)


class Solution2(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Two pointers method
        vowels = set("aeiouAEIOU")
        s = list(s)  # 一定要换成list
        l, r = 0, len(s)-1
        while l <= r:
            while s[l] not in vowels and l < r:
                l += 1
            while s[r] not in vowels and l < r:
                r -= 1
            if l > r:
                break
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
        return "".join(s)
