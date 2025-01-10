class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:

        n = len(s)
        # dp = [[] * n for _ in range(n)]
        d = [0] * (n + 1)
        value = 0
        for i in range(n - 1, -1, -1):
            if value + int(s[i]) * 2**(n-i-1) <= k:
                d[i] = d[i+1] + 1
                value = value + int(s[i]) * 2**(n-i-1)
            else:
                d[i] = d[i+1]

        return d[0]

