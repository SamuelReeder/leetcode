class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        
        m = len(mat)
        n = len(mat[0])

        if m * n != r * c:
            return mat

        total = m * n

        res = [[0 for _ in range(c)] for _ in range(r)]
        for i in range(total):

            x = i // n
            y = i % n

            tmp = mat[x][y]

            x = i // c
            y = i % c

            res[x][y] = tmp

        return res
