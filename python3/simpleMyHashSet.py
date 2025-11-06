class MyHashSet:

    # basically we need a mapping of item -> index
    # given the item, we can deterministically grab index
    def __init__(self):
        self.items = [False] * (10**6 + 1)

    def add(self, key: int) -> None:
        
        self.items[key] = True    

    def remove(self, key: int) -> None:
        self.items[key] = False

    def contains(self, key: int) -> bool:
        return self.items[key]


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
