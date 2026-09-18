class Solution:
    def minOperations(self, nums: List[int]) -> int:
        
        n = len(nums)
        res = 0
        for i in range(1, n):
            tmp = nums[i - 1] - nums[i] + 1
            if tmp > 0:
                res += tmp
                nums[i] += tmp

        return res
