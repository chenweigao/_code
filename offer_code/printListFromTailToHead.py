"""
输入一个链表，按链表从尾到头的顺序返回一个ArrayList。

这道题目相当于逆序一个链表，但是可以有额外的存储空间
"""
# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead_array(self, listNode):
        # write code here
        res = []
        cur = listNode
        while cur:
            res.append(cur.val)
            cur = cur.next
        return res[::-1]

    def printListFromTailToHead(self, listNode):
        res = []
        cur = listNode
        while cur:
            res.append_left(cur.val)
            cur = cur.next
        return res[::-1]
        
