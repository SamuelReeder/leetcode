class Solution:
    def numberOfGoodSubarraySplits(self, nums: List[int]) -> int:
        
        MOD = (10**9 + 7)

        if 1 not in nums:
            return 0

        res = 1
        current = None
        for i in range(len(nums)):
            # at each iter, we include the number of subarrays ending at i

            if nums[i]:
                if current is not None:
                    res = res * max((i - current), 1) % MOD
                current = i
            
        return res



        
