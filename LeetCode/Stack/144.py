# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class SolutionRecurse:
    def preorderTraversal(self, root: 'TreeNode') -> 'List[int]':
        ans = []
        self.recurse(root, ans)
        return ans

    def recurse(self, root, ans):
        if root:
            ans.append(root.val)
            self.recurse(root.left, ans)
            self.recurse(root.right, ans)


class SolutionIter:
    def preorderTraversal(self, root: 'TreeNode') -> 'List[int]':
        st = []
        ans = []
        while True:
            while root:
                ans.append(root.val)
                st.append(root)
                root = root.left
            if not st:
                return ans
            root = st.pop()
            root = root.right


class Solution:
    def preorderTraversal(self, root: 'TreeNode') -> 'List[int]':
        st = [root]
        ans = []
        while st:
            node = st.pop()
            if node:
                ans.append(node.val)
                st.append(node.right)
                st.append(node.left)
        return ans
