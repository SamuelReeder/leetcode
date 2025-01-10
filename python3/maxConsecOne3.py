class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        
        highest = 0
        zeros = 0
        while k > zeros and highest < len(nums):
            if nums[highest] == 0:
                zeros += 1
            highest += 1
        
        i = 0
        for j in range(highest, len(nums)):
            if nums[j] == 0:
                i = nums.index(0, i) + 1
            highest = max(highest, j + 1 - i)

        return highest
                


