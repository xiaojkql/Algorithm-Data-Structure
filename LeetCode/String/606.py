# 606. Construct String from Binary Tree
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def tree2str(self, t):

        def recurse(t):
            if not t:
                return ""  # 递归基
            ans = str(t.val)
            if t.left:
                ans += "(" + recurse(t.left) + ")"  # 如果存在左孩子就往左边去
            if not t.left and t.right:
                ans += "()"
            if t.right:  # 如果存在右孩子就往右边去
                ans += "("+recurse(t.right)+")"
            return ans  # 左右遍历完毕后就返回answer
        ans = recurse(t)
        return ans
