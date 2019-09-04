class LinkedList(object):
    def __init__(self):
        self.head = None

    class Node(object):
        def __init__(self, data):
            self.data = data
            self.next = None

    def swap_nodes(self, x, y):
        if x == y:
            return
        
        prevX = None
        currX = self.head
        while currX != None and currX.data != x:
            prevX = currX
            currX = currX.next

        prevY = None
        currY = self.head
        while currY != None and currY.data != y:
            prevY = currY
            currY = currY.next

        if currX == None or currY == None:
            return
        
        '''
        conclusion:
        1. prevX.next -> currY
        2. prevY.next -> currX
        3. swap the next points
            - temp = currX.next
            - currX.next = currY.next
            - currY.next = temp
        '''

        # x is not head of linked list
        if prevX != None:
            prevX.next = currY
        else:
            self.head = currY

        if prevY != None:
            prevY.next = currX
        else:
            self.head = currX

        temp = currX.next
        currX.next = currY.next
        currY.next = temp

    def push(self, new_data):
        new_node = self.Node(new_data)
        # make next of new node as head
        new_node.next = self.head
        self.head = new_node

    def createLinkedList(self, nums):
        new_node = self.Node(nums[0])
        self.head = new_node
        cur = self.head
        for num in nums[1:]:
            node = self.Node(num)
            cur.next = node
            cur = cur.next
        

    def printList(self):
        t_node = self.head
        while t_node != None:
            print(t_node.data, end = '->')
            t_node = t_node.next
        print('\n')


llist = LinkedList() 
  
# The constructed linked list is: 
# 1->2->3->4->5->6->7 
# llist.push(7) 
# llist.push(6) 
# llist.push(5) 
# llist.push(4) 
# llist.push(3) 
# llist.push(2) 
# llist.push(1) 
llist.createLinkedList([1,2,3,4,5,6,7,8])
llist.printList() 
llist.swap_nodes(3, 5) 
llist.printList()
