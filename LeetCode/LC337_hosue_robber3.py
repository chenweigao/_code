from collections import deque

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None



class Solution:
    def rob(self, root: TreeNode):
        '''
        思路整理：
        1. 该题目实际上是一个 DFS, 每次只能遍历一层，相邻的层不能遍历
        2. 在此条件下，求能遍历的层数的最大值
        3. 简单的思路是：两种情况，第 1 层是否被遍历？
            - 被遍历，则遍历 1, 3, 5... 直到结束
            - 不被遍历，则遍历 2, 4, 6... 直到结束
        4. 如何计算二叉树的层数？或者 不计算，改计算每一层的节点数：1: 1, 2: 2, 3: 4, 4: 8, n: 2^n-1(从 1 开始计数)
        '''
        if not root:
            return 0

        res = 0
        if root.left:
            res += self.rob(root.left.left) + self.rob(root.left.right)
        if root.right:
            res += self.rob(root.right.left) + self.rob(root.right.right)

        return max(res + root.val, self.rob(root.left) + self.rob(root.right))

data = [3,2,3,None,3,None,1]

print(Solution().rob(data))