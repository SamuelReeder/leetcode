class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        # sort?
        n = len(rocks)
        for i in range(n):
            capacity[i] -= rocks[i]

        capacity.sort()
        res = 0 
        for cnt in capacity:
            additionalRocks -= cnt
            if additionalRocks < 0:
                break
            res += 1

        return res
            
