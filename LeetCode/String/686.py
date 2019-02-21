# 686. Repeated String Match
class Solution(object):
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        orA, count = A, 1
        while len(A) < len(B):
            A, count = orA + A, count + 1
        if B in A:
            return count
        if B in A + orA:
            return count + 1
        return -1


class Solution(object):
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        n = -((-len(B)) // len(A))  # 整除的应用
        return n*(B in A*n) or (n+1) * (B in A*(n+1)) or -1
