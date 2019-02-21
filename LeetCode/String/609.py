# 609. Find Duplicate File in System
class Solution(object):
    def findDuplicate(self, paths):
        """
        :type paths: List[str]
        :rtype: List[List[str]]
        """
        dic = {}
        for path in paths:
            path = path.split()
            root = path[0]
            for item in path[1:]:
                content = item.split("(")
                if content[-1] not in dic:
                    dic[content[-1]] = []
                dic[content[-1]].append((root+"/"+content[0]))
        ans = [item for key, item in dic.items() if len(item) > 1]
        return ans
