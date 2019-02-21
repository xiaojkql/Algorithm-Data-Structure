# 833. Find And Replace in String
class Solution(object):
    def findReplaceString(self, S, indexes, sources, targets):
        """
        :type S: str
        :type indexes: List[int]
        :type sources: List[str]
        :type targets: List[str]
        :rtype: str
        """
        arr, dic = [], dict(zip(indexes, zip(sources, targets)))  # 自动
        i = 0
        while i < len(S):
            if i in dic.keys():
                s, t = dic[i]
                if s == S[i:i+len(s)]:
                    arr.append(t)
                    i += len(s)
                else:
                    arr.append(S[i])
                    i += 1
            else:
                arr.append(S[i])
                i += 1
        return "".join(arr)
