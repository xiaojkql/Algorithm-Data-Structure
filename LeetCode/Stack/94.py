# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def inorderTraversalIter(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        st = []
        ans = []
        while True:
            while root:
                st.append(root)
                root = root.left
            if not st:
                return ans
            root = st.pop()
            ans.append(root.val)
            root = root.right


class SolutionRecurse:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ans = []
        self.recurse(root, ans)
        return ans

    def recurse(self, root, ans):
        if root:
            self.recurse(root.left, ans)
            ans.append(root.val)
            self.recurse(root.right, ans)
