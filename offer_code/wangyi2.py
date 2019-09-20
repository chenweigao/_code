# coding: utf8
"""
单链表定义如下：
class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None
"""

class Solution(object):
    def removeDuplicates(self, head):
        """
        :type head: ListNode
        """
        # 在这里编写代码
        cur = head
        while cur and cur.next.next:
            if cur.val != cur.next.next.val:
                cur = cur.next
            else:
                cur.next = cur.next.next
                
        return head