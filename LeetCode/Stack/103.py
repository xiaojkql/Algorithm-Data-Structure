# 103. Binary Tree Zigzag Level Order Traversal

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        ans, level, directions = [], [root], 1
        while level:
            ans.append([node.val for node in level[::directions]])
            directions *= -1
            level = [kid for node in level for kid in [
                node.left, node.right] if kid]
        return ans
