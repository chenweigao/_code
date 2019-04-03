'''
1 -> 2 -> 3 -> null

null -> 3 -> 2 -> 1
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pre = None # 这个 None 不好理解的话拿一个中间节点看
        cur = head

        while cur is not None:
            next = cur.next  # 存储 cur 的下一个节点，避免下次找不到
            cur.next = pre  # 指向前面的节点
            pre = cur  # 向后遍历
            cur = next  # 向后遍历
        return pre

    def reverseList2(self, head):
        if head is None or head.next is None:
            return head
        p = self.reverseList2(head.next)
        head.next.next = head # head 的 next 节点指向 head
        head.next = None
        return p