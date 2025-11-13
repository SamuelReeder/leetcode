class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        

        mask = 0
        dup = 0
    
        for num in nums:

            mask = (mask ^ num) & ~dup
            dup = (dup ^ num) & ~mask
            
        return mask
