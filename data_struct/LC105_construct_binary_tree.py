# Definition for a binary tree node.
#Construct Binary Tree from Preorder and Inorder Traversal

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


'''
build tree via preorder and inorder traversal
preorder = [3, 9, 20, 15, 7] root left right
inorder = [9, 3, 15, 20, 7]  left root right

what is the tree should be?
'''
class Solution:
    def buildTree(self, preorder: 'List[int]', inorder: 'List[int]') -> TreeNode:
        if not preorder or not inorder:
            return None
        
        # find the root
        root = TreeNode(preorder.pop(0))

        # the what to do? recursive?
        inorder_index = inorder.index(root.val)

        root.left = self.buildTree(preorder, inorder[:inorder_index])
        root.right = self.buildTree(preorder, inorder[inorder_index + 1:])

        return root
        