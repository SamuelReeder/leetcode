class RecentCounter:

    def __init__(self):
        self.last = 0
        self.arr = []

    def ping(self, t: int) -> int:
        self.arr.append(t)
        for i in range(self.last, len(self.arr)):
            if t - self.arr[i] <= 3000:
                self.last = i
                break
        
        return len(self.arr) - self.last

        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
