class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) < 2:
            return nums[0]

        d = [0] * len(nums)
        d[0] = nums[0]
        d[1] = max(nums[1], nums[0])

        for i in range(2, len(nums)):
            d[i] = max(d[i - 1], d[i - 2] + nums[i])

        return d[-1]

            
        
