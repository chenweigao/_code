# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


'''
given inorder and postorder

inorder = [9, 3, 15, 20, 7]   left root right
postorder = [9, 15, 7, 20, 3] left right root

return the tree
'''


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not inorder or not postorder:
            return None

        # find the root first
        root = TreeNode(postorder.pop())

        inorder_index = inorder.index(root.val)

        root.right = self.buildTree(inorder[inorder_index + 1:], postorder)
        root.left = self.buildTree(inorder[:inorder_index], postorder)

        return root
