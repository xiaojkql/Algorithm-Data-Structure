# 145. Binary Tree Postorder Traversal

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def recurse(node, ans):
            if node:
                if node.left:
                    recurse(node.left, ans)
                if node.right:
                    recurse(node.right, ans)
                ans.append(node.val)

        ans = []
        recurse(root, ans)
        return ans
