class Node:
    def __init__(self, val):
        self.val = val
        self.parent = None
        self.children = []


def createParent(n, nums):
    node = Node(n)
    node.parent = None
    for num in nums:
        node.children.append(num)
    return node


def addChildren(node, children:'List'):
    for n in children:
        temp = Node(n)
        temp.parent = node
        node.children.append(temp)
    return node


nums = [1, 2, 3, 4, 5]

node = Node(0)
addChildren(node, nums)
print(node.children)
