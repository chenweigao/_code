class Node(object):
    val = None
    next = None


def swapLinkedList(head, m, n):
    res = []
    cur = head
    while cur:
        # print(cur.val)
        res.append(cur.val)
        cur = cur.next
    res[m - 1], res[n - 1] = res[n - 1], res[m - 1]
    # print(res)
    ans = createLinkedList(res)
    return ans



def printLinkedList(head):
    cur = head
    while cur.next is not None:
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

nums = [11, 5, 8, 22, 9, 5]

alinked_list = createLinkedList(nums)
printLinkedList(alinked_list)
# res = swapLinkedList(alinked_list, 3, 5)
# print(swapLinkedList(alinked_list, 3, 5))
# printLinkedList(swapLinkedList(alinked_list, 3, 5))
# printLinkedList(res)
