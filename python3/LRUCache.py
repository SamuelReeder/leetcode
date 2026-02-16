from collections import deque

class Node:
    def __init__(self, key = None, value = None):
        self.next = None
        self.prev = None
        self.key = key
        self.val = value

class LRUCache:

    # hashmap of key -> value
    # len of map dictates size
    # DLL will dictate LRU
    # tail is most recent

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hm = dict()
        self.tail = Node()
        self.head = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def add(self, node):
        prev = self.tail.prev
        self.tail.prev = node
        node.next = self.tail
        node.prev = prev
        prev.next = node

    def remove(self, node):
        node.next.prev = node.prev
        node.prev.next = node.next

    def get(self, key: int) -> int:
        if key not in self.hm:
            return -1

        # dict is key to node
        node = self.hm[key]
        self.remove(node)
        self.add(node)
        
        return node.val        

    def put(self, key: int, value: int) -> None:
        if len(self.hm) == self.capacity and key not in self.hm:
            # evict
            del self.hm[self.head.next.key]
            self.remove(self.head.next)
            
        if key in self.hm:
            node = self.hm[key]
            self.remove(node)
            self.add(node)
            node.val = value
        else:
            self.hm[key] = Node(key, value)
            self.add(self.hm[key])


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
