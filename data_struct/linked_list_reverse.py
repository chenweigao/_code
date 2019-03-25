'''
1 -> 2 -> 3 -> null

null -> 3 -> 2 -> 1
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def reverseList(self, head):
        # try an iterive solution
        preNode = None
        curNode = head

        while curNode.next is not None:
            next = curNode.next
            curNode.next = preNode
            preNode = curNode
            curNode = next

        return preNode