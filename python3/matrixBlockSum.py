class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        
        # rows, cols
        m, n = len(mat), len(mat[0])

        # index mat by r, c
        # for each i, j in answer
        # i - k <= r <= i + k (basically a range of rows with padding)
        # j - k <= c <= j + k (basically a range of columns with padding)

        answer = [[0 for _ in range(n)] for _ in range(m)]
        dp = [[0 for _ in range(n)] for _ in range(m)]

        def safe_index(i, j):
            if i < 0 or j < 0:
                return 0
            
            return dp[min(i, m - 1)][min(j, n - 1)]

        for i in range(m):
            for j in range(n):
                dp[i][j] = safe_index(i, j - 1) - safe_index(i - 1, j - 1) + safe_index(i - 1, j) + mat[i][j]

        for i in range(m):
            for j in range(n):
                 answer[i][j] = safe_index(i + k, j + k) - safe_index(i - k - 1, j + k) - safe_index(i + k, j - k - 1) + safe_index(i - k - 1, j - k - 1)

        return answer



