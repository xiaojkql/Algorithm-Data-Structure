# 916. Word Subsets
class Solution(object):
    def wordSubsets(self, A, B):
        """
        :type A: List[str]
        :type B: List[str]
        :rtype: List[str]
        """
        dic = {}
        for s in B:
            for ch in s:
                dic[ch] = max(dic.get(ch, 0), s.count(ch))
        print(dic)
        ans = []
        for s in A:
            sa = False
            for ch in dic.keys():
                if ch in s:
                    if s.count(ch) < dic[ch]:
                        sa = True
                        continue
                else:
                    sa = True
                    continue
            if sa:
                continue
            else:
                ans.append(s)
        return ans


class Solution(object):
    def wordSubsets(self, A, B):
        """
        :type A: List[str]
        :type B: List[str]
        :rtype: List[str]
        """
        dic = {}
        for s in B:
            for ch in s:
                dic[ch] = max(dic.get(ch, 0), s.count(ch))
        print(dic)
        ans = []
        for s in A:
            if all(s.count(ch) >= dic[ch] for ch in dic.keys()):
                # 用一个all函数解决了很多代码
                ans.append(s)
        return ans
