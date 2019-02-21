# 890. Find and Replace Pattern
class Solution(object):
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        def isMatch(word):
            if len(word) != len(pattern):
                return False
            if len(set(word)) != len(set(pattern)):
                return False
            dic = {}  # 建立一个映射函数
            for w, p in zip(word, pattern):
                if p not in dic:
                    dic[p] = w  # 建立映射
                if w != dic[p]:
                    return False
            return True
        ans = []
        for word in words:
            if isMatch(word):
                ans.append(word)
        return ans


class Solution(object):
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        def isMatch(word):
            return (len(word) == len(pattern) and
                    (len(set(word)) == len(set(pattern)) ==
                     len(set([(a, b) for a, b in zip(word, pattern)]))
                     == len(set(word))))
        return filter(isMatch, words)


class Solution(object):
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        def isMatch(word):
            dic = {}
            ans = []
            for ch in word:
                ans.append(dic.setdefault(ch, len(dic)))
            return ans
        return [word for word in words if isMatch(word) == isMatch(pattern)]
