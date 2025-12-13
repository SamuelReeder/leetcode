class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
                
        n = len(energy)
        dp = [0] * n

        m = energy[-1]
        for i in range(n - 1, -1, -1):
            
            if n - i - 1 < k:
                dp[i] = energy[i] 
            else:
                dp[i] = dp[i + k] + energy[i]

            m = max(dp[i], m)

        return m
