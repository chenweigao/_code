class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def listToTreeNode(nums):
        root = TreeNode(nums[0])
        nodeQueue = [root]
        front = 0
        index = 1
        while index < len(nums):
            node = nodeQueue[front]
            front += 1

            item = nums[index]
            index += 1
            if item != 'null':
                leftNum = int(item)
                node.left = TreeNode(leftNum)
                nodeQueue.append(node.left)

            if index >= len(nums):
                break

            item = nums[index]
            index += 1
            if item != 'null':
                rightNum = int(item)
                node.right = TreeNode(rightNum)
                nodeQueue.append(node.right)
        return root
