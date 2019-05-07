# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sortedArrayToBST(self, nums: 'List[int]') -> TreeNode:
        if not nums:
            return None

        l, r = 0, len(nums) - 1

        mid = (l + r) // 2

        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid + 1:])

        return root


class Solution2:
    def sortedArrayToBST(self, nums: 'List[int]') -> TreeNode:
        if not nums:
            return None

        return self.helper(nums, 0, len(nums) - 1)

    def helper(self, nums, l, r):

        if l > r:
            return None
        mid = (r + l) // 2

        node = TreeNode(nums[mid])
        node.left = self.helper(nums, l, mid - 1)
        node.right = self.helper(nums, mid + 1, r)
        return node
