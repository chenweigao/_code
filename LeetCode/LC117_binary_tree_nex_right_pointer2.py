# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


'''
the question is simply different, where the tree is nolonger prefect binary tree
'''


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None

        
        return root
