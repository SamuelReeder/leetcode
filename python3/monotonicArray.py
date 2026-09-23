class Solution:
    def isMonotonic(self, nums: list[int]) -> bool:
        last = nums[0]
        is_decreasing = None
        for i, num in enumerate(nums[1:]):
            if num == last:
                pass
            elif is_decreasing is None:
                is_decreasing = num < last
            elif is_decreasing != (num < last):
                return False
            
            last = num
        
        return True
