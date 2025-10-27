class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        
        # can use dp with bottom right of submatrix
        n = len(grid)
        m = len(grid[0])
        dp = [[0] * m for _ in range(n)]

        res = 0
        for i in range(n):
            for j in range(m):
                
                total = 0

                if i > 0 and j > 0:
                    total += dp[i - 1][j] + dp[i][j-1] - dp[i-1][j-1]
                elif i > 0:
                    total += dp[i - 1][j]
                elif j > 0:
                    total += dp[i][j - 1]

                dp[i][j] += total + grid[i][j]

                if dp[i][j] <= k:
                    res += 1
                else:
                    break

        return res

