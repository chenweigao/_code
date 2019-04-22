# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        
        queue = [root]
        while queue:
            q = []
            pre = None
            for node in queue:
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

                if pre:
                    pre.next = node
                pre = node
            queue = q
        return root
           