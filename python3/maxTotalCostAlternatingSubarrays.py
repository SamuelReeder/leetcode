class Solution:
    def maximumTotalCost(self, nums: List[int]) -> int:
        add_sum = nums[0]
        sub_sum = -float('inf') 
        
        for i in range(1, len(nums)):
            x = nums[i]
                        
            add_sum, sub_sum = max(add_sum, sub_sum) + x, add_sum - x
            
        return max(add_sum, sub_sum)
