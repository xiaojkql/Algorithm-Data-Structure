# 331. Verify Preorder Serialization of a Binary Tree


class SolutionBrilliantIdea(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        strLs = preorder.split(",")
        diff = 1
        for ch in strLs:
            diff -= 1
            if diff < 0:
                return False
            if ch != "#":
                diff += 2
        return diff == 0


# 思想：
# 将树从下而上两两进行合并，最后仅剩一个根节点
class SolutionStack(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        strLs = preorder.split(",")
        st = []
        for ch in strLs:
            st.append(ch)
            while len(st) > 1 and st[-1] == "#" and st[-2] == "#":
                st.pop()
                st.pop()
                if not st:
                    return False
                st[-1] = "#"
        return st == ["#"]
