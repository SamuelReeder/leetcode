class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        
        n, m = len(mat), len(mat[0])
        eligible = [True] * 4
        for i in range(n):
            for j in range(m):
                
                if eligible[0]:
                    eligible[0] = mat[i][j] == target[i][j]
                
                if eligible[1]:
                    eligible[1] = mat[i][j] == target[j][n - 1 - i]
                
                if eligible[2]:
                    eligible[2] = mat[i][j] == target[m - 1 - i][n - 1 - j]

                if eligible[3]:
                    eligible[3] = mat[i][j] == target[m - 1 - j][i]
        
        return True in eligible



