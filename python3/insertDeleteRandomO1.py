class RandomizedSet:

    def __init__(self):
        self.l = []
        self.d = {}

    def insert(self, val: int) -> bool:
        if val in self.d:
            return False
        self.d[val] = len(self.l)
        self.l.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.d:
            return False
        last = self.l[-1]
        remove = self.l[self.d[val]]
        self.l[self.d[val]] = last
        self.d[last] = self.d[val]
        del self.d[val]
        self.l[-1] = remove
        self.l.pop()
        return True

    def getRandom(self) -> int:
        return random.choice(self.l)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
