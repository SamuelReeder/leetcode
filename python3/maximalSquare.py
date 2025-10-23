class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        
        n = len(matrix)
        m = len(matrix[0])

        maximum = 0

        dp = [[0] * m for _ in range(n)]
        for i in range(n):
            dp[i][0] = int(matrix[i][0])
            maximum = max(maximum, dp[i][0])

        for j in range(m):
            dp[0][j] = int(matrix[0][j])
            maximum = max(maximum, dp[0][j])

        # loop through each top left index
        for i in range(1, n):  # rows
            for j in range(1, m): # cols


                # each entry of dp shows the size of the square ending at i, j

                num = int(matrix[i][j])
                
                if num == 1:
                    square = min(dp[i - 1][j], dp[i - 1][j - 1], dp[i][j - 1])
                    dp[i][j] = square + 1
                    maximum = max(maximum, dp[i][j])
                else:
                    dp[i][j] = 0
                    
        return maximum**2
            

