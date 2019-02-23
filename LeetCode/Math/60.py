# 60. Permutation Sequence
class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        ls = [i for i in range(1, n+1)]
        ans = []
        fac, x = 1, n
        k = k-1
        while x:
            fac *= x
            x = x-1
        for i in range(n, 0, -1):
            fac //= i
            index = k // fac
            k = k - index*fac
            ans.append(str(ls.pop(index)))
        return "".join(ans)


if __name__ == "__main__":
    sol = Solution()
    print(sol.getPermutation(4, 14))
