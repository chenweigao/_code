class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.value = None


class Solution:
    def solution(self, array):
        temp = []
        for node_list in array:
            node = Node(node_list[0])
            node.next = node_list[1]
            node.value = node_list[2]
         
            temp.append(node)
        ret = []
        for node in temp:
            temp_max = node.value
            if node.next:
                temp_max = max(temp_max, node.value + temp_max)
                


