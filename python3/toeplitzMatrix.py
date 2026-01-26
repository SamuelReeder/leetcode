class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        
        n, m = len(matrix), len(matrix[0])
        for i in range(1, n):
            for j in range(1, m):
                if matrix[i][j] != matrix[i - 1][j - 1]:
                    return False

        return True
