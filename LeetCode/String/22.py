# 22. Generate Parentheses
# 使用递归，backtracking进行解决


class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def recurse(ans, s, left, right):
            if left > right:
                return
            if left == right == 0:
                ans.append(s)
            if left > 0:
                recurse(ans, s+'(', left-1, right)
            if right > 0 and right > left:
                recurse(ans, s+")", left, right-1)
        ans, s, left, right = [], "", n, n
        recurse(ans, s, left, right)
        return ans
