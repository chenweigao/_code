class Node:
    
    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.size = 0

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index < 0 or index >= self.size:
            return - 1
            
        if self.head is None:
            return - 1
        curr =self.head
        for i in range(index):
            curr = curr.next
        return curr.val

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        node = Node(val)
        node.next = self.head
        self.head = node
        
        self.size += 1

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        curr = self.head
        if curr is None:
            self.head = Node(val)
        else:
            while curr.next is not None:
                curr = curr.next
            curr.next = Node(val)

        self.size += 1

        
    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index < 0 or index > self.size:
            return
        if index == 0:
            self.addAtHead(val)
        else:
            cur = self.head
            for i in range(index - 1):
                cur = cur.next
            node = Node(val)
            node.next = cur.next
            cur.next = node
            self.size += 1


    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index < 0 or index >= self.size:
            return

        cur = self.head

        if index == 0:
            self.head = cur.next
        else:
            for i in range(index - 1):
                cur = cur.next
            cur.next = cur.next.next
        self.size -= 1


        def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
            slow = fast = head
            for i in range(n):
                fast = fast.next
                
            if not fast:
                return head.next
            
            while fast.next is not None:
                fast = fast.next
                slow = slow.next
            slow.next = slow.next.next
            return head
# Your MyLinkedList object will be instantiated and called as such:
obj = MyLinkedList()
obj.addAtHead(1)
# obj.addAtTail(2)
obj.addAtIndex(1,2)
param_1 = obj.get(1)
param_2 = obj.get(0)
param_3 = obj.get(2)
# obj.deleteAtIndex(0)
print(param_3)