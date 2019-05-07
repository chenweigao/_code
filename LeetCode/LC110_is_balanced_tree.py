# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        if abs(self.getHeight(root.right) - self.getHeight(root.left)) > 1:
            return False
        return self.isBalanced(root.right) and self.isBalanced(root.left)

    def getHeight(self, root):
        if root is None:
            return 0
        return max(self.getHeight(root.left), self.getHeight(root.right)) + 1


class Solution2:
    def isBalanced(self, root: TreeNode) -> bool:
        r = True

        def helper(root):
            nonlocal r
            if root is None:
                return 0
            left = helper(root.left)
            right = helper(root.right)

            if abs(left - right) > 1:
                r = False

            return max(left, right) + 1

        helper(root)
        return r
