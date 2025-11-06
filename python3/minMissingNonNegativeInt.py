class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        # we want to make the mex maximal
        
        # could use a hash map to keep track of each value

        # we can do element % mex to get the lowest
        
        hm = {}
        for idx, i in enumerate(nums):
            v = i % value
            # for negative we need to add value again
            if v < 0:
                v += value
            
            if v in hm:
                hm[v] += 1
            else:
                hm[v] = 1
            
            nums[idx] = v * hm[v]

        i = 0
        while True:
            v = i % value
            mult = i // value
            if v not in hm:
                return i

            if hm[v] <= mult:
                return i

            i += 1 

        

        
