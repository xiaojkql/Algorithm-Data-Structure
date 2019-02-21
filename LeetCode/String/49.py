# 49. Group Anagrams
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        ans = {}
        for word in strs:
            key = tuple(sorted(word))
            ans[key] = ans.get(key, []) + [word]
        return ans.values()
