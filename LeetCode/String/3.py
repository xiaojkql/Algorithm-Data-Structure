# 3. Longest Substring Without Repeating Characters
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxLen, currLen, iS = 0, 0, 0
        while iS < len(s):
            currI, currLen, currSet = iS, 0, set()
            while currI < len(s):
                currSet.add(s[currI])
                if len(currSet) != currLen+1:
                    break
                else:
                    currLen, currI = currLen+1, currI+1
            if maxLen < currLen:
                maxLen = currLen
            iS += 1
        return maxLen


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 思想一当前新的字符为结束的为重复子串的最大长度
        lastSeen, maxLen, start = {}, 0, 0
        for i in range(len(s)):
            if s[i] in lastSeen and start <= lastSeen[s[i]]:
                start = lastSeen[s[i]]+1
            else:
                maxLen = max(maxLen, i-start+1)
            lastSeen[s[i]] = i
        return maxLen
