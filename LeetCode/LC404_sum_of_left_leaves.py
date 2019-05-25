# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:

        self.res = 0

        def dfs(root):
            if not root:
                return 0
            if root.left and not root.left.left and not root.left.right:
                self.res += root.left.val
            dfs(root.right)
            dfs(root.left)
        dfs(root)
        return self.res
