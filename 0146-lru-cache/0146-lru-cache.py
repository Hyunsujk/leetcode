class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def _remove(self, node):
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p
    
    def _add(self, node):
        last = self.tail.prev
        last.next = node
        node.prev = last
        node.next = self.tail
        self.tail.prev = node
        

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._add(node)
            return node.val
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            node.val = value
            self._add(node)
        else:
            node = Node(key, value)
            self._add(node)
            self.cache[key] = node
        
        if len(self.cache) > self.capacity:
            while len(self.cache) > self.capacity:
                lru = self.head.next
                self._remove(lru)
                self.cache.pop(lru.key)

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)