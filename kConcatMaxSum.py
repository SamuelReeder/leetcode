class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        MOD = (10**9 + 7)
        n = len(arr)

        max_sum = curr = 0
        for i in range(n * min(2, k)):
            j = i % n
            
            curr = max(curr + arr[j], arr[j])
            max_sum = max(max_sum, curr)

        alt = max_sum + sum(arr) * (k - 2) if k >= 2 else 0
        return max(max_sum, alt) % MOD
            




        
