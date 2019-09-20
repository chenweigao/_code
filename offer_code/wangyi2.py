# coding: utf8
"""
单链表定义如下：
class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None
"""
class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution(object):
    def removeDuplicates(self, head):
        """
        :type head: ListNode
        """
        # 在这里编写代码
        if not head or not head.next:
            return head
        dummy = ListNode(-1)
        dummy.next = head
        pre = dummy
        while pre.next and pre.next.next:
            cur = pre.next
            if cur.val == cur.next.next.val:
                cur.next.next = cur.next.next.next
                cur.next.next.next = None
            else:
                cur = cur.next
        return dummy.next
                
alist = [1, 2, 2, 2, 2, 3, 3, 4, 5, 5, 5]

head = ListNode(alist[0])
for num in alist:
    node = ListNode(num)
    head.next = node
    head = head.next

node = Solution().removeDuplicates(head)
cur = node
while cur.next:
    print(cur.val)
    cur = cur.next