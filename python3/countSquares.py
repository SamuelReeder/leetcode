class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        
        n = len(matrix)
        m = len(matrix[0])

        count = 0

        dp = [[0] * m for _ in range(n)]
        # loop through each top left index
        for i in range(n):  # rows
            for j in range(m): # cols


                # each entry of dp shows the size of the square ending at i, j

                num = matrix[i][j]
                
                if num == 1:
                    square = 0 if i == 0 or j == 0 else min(dp[i - 1][j], dp[i - 1][j - 1], dp[i][j - 1]) 
                    dp[i][j] = square + 1
                    count += dp[i][j] 
                else:
                    dp[i][j] = 0
                    
        return count

        





