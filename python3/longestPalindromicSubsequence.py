class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        if n == 1:
            return 1
        
        dp = [[-1 for _ in range(n)] for _ in range(n)]


        # need to compute longest substrings by having indices i and j 
        # that already have a x longest substring, and then checking if 
        # i - 1 and j + 1 are same and adding that for next 
        # longest = dp[i + 1, j - 1] + (2 if s[j] == s[i] else 0)
        # compute smaller values of i and j first

        for i in range(n):
            dp[i][i] = 1

        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    if j - i == 1:
                        dp[i][j] = 2
                    else:
                        dp[i][j] = 2 + dp[i + 1][j - 1] 
                else:
                    if j - i == 1:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])              

        return dp[0][n-1]
            


