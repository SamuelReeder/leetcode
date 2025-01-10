class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        
        import math
        
        largest = -1 * math.inf 
        current = 0
        for i in nums:
            current += i
            largest = max(current, largest)
            if current < 0:
                current = 0
            
        
        return largest
            



        
