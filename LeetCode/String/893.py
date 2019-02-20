class Solution(object):
    def numSpecialEquivGroups(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        aSet = set()
        for a in A:
            odd = "".join(sorted(a[0::2]))
            even = "".join(sorted(a[1::2]))
            aSet.add((even, odd))
        return len(aSet)
        # return len({tuple(("".join(sorted(a[0::2])),
        # "".join(sorted(a[1::2]))))
        # for a in A})
        # 使用这些方法时一定要注意是可迭代对象
