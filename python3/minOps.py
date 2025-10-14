class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        
        # we xor each 
        mask = 0
        for i in nums:
            mask ^= i

        ops = 0
        i = 0
        
        loop = max(mask, k)
        while loop > 0:
            if k & 1 != mask & 1:
                ops += 1

            k >>= 1
            mask >>= 1
            loop >>= 1
            
            i += 1

        return ops

