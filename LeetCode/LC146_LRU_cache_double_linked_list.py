
class Node:
    def __init__(self, k: int, v: int):
        self.key = k
        self.value = v
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.dic = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.dic:
            self._remove(self.dic[key])
            self._add(self.dic[key])
            return self.dic[key].value
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            self._remove(dic[key])
        n = Node(key, value)
        self._add(n)
        self.dic[key] = n
        if len(self.dic) > self.capacity:
            first_node = self.head.next
            self._remove(first_node)
            del self.dic[first_node.key]

    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def _add(self, node):
        node.prev = self.tail.prev
        self.tail.prev = node
        node.next = self.tail
        

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)