class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
            
        n = len(nums)
        dp = [1] * n
        cnt = [1] * n 
        
        longest = 1
        
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        cnt[i] = cnt[j]
                    elif dp[j] + 1 == dp[i]:
                        cnt[i] += cnt[j]
            if dp[i] > longest:
                longest = dp[i]
                
        res = 0
        for i in range(n):
            if dp[i] == longest:
                res += cnt[i]
                
        return res
