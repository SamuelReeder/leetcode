class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # robot has to move m - 1 down and n - 1 right
        # its basically the number of combinations
        # dp is number of ways to get to any cell i, j
        # dp[j][i] = dp[j][i + 1] + dp[j - 1][i] + 2

        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[0] = [1 for _ in range(n)]
        for i in range(m):
            dp[i][0] = 1

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[m-1][n-1]
