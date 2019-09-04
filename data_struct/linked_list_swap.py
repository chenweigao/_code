class Node(object):
    val = None
    next = None


def swapLinkedList(head, m, n):
   return None



def printLinkedList(head):
    cur = head
    while cur is not None:
        print(cur.val)
        cur = cur.next

def createLinkedList(nums):
    head = Node()
    head.val = nums[0]
    cur = head
    for num in nums[1:]:
        node = Node()
        node.val = num
        cur.next = node
        cur = cur.next
    return head

def findPrevNode(head, num) -> 'Node':
    cur = head
    while cur and cur.next:
        if cur.next.val == num:
            return cur
        cur = cur.next
    return None

nums = [11, 5, 8, 22, 9, 5]

# swap linkedlist at index 3 and 5

alist = createLinkedList(nums)

swapLinkedList(alist, 8, 9)
# prev_a = findPrevNode(alist, 8)
# prev_b = findPrevNode(alist, 9)

# prev_a.next.val, prev_b.next.val = prev_b.next.val, prev_a.next.val

printLinkedList(alist)

# printLinkedList(alist)