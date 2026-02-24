class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # robot has to move m - 1 down and n - 1 right
        # its basically the number of combinations
        # dp is number of ways to get to any cell i, j
        # dp[j][i] = dp[j][i + 1] + dp[j - 1][i] 

        m, n = len(obstacleGrid), len(obstacleGrid[0])

        dp = [[0 for _ in range(n)]  for _ in range(m)]
        for i in range(n):
            if obstacleGrid[0][i] == 1:
                break
            dp[0][i] = 1

        for i in range(m):
            if obstacleGrid[i][0] == 1:
                break
            dp[i][0] = 1

        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[m-1][n-1]
