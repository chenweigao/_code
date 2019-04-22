# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


'''
make a collection with left node and right node, how to do it?
root.left.next -> root.right
root.right.next -> None

for a node, if it has next node, then p.right.next = p.next.left

because the tree is prefet binary tree, so we visit the left node is enough
'''


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None

        if root.left:
            root.left.next = root.right
            if root.next:
                root.right.next = root.next.left

            self.connect(root.left)
            self.connect(root.right)
        return root
