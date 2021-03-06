import sys
sys.path.append(r'C:\\Users\\nerche\\Documents\\_code\\LeetCode\\_include')
import treenode

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 使用递归求解
class Solution:
    def inorderTraversal(self, root):
        res = []
        self.inorder(root, res)
        return res

    def inorder(self, root, res):
        if not root:
            return
        if root.left:
            self.inorder(root.left, res)
        # print("root.val:", root.val)
        res.append(root.val)
        if root.right:
            self.inorder(root.right, res)

class Solution2:
    def inorderTraversal(self, root):
        res = []
        stack = []
        p = root

        while p and stack:
            if p:
                stack.append(p)
                p = p.left
            else:
                p = stack[-1]
                stack.pop()
                res.append(p.val)
                p = p.right
        return res


class MorrisTraversal:
    def inorderTraversal(self, root):
        

nums = [10, 5, 12, 1, 6, 11]

root = treenode.TreeNode.listToTreeNode(nums)

res = Solution2().inorderTraversal(root)
print(res)
