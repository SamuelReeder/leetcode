class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])

        loc = dict()

        rows = [0] * m 
        cols = [0] * n

        for i, row in enumerate(mat):
            for j, col in enumerate(row):
                loc[col] = (i, j)

        for idx, num in enumerate(arr):
            i, j = loc[num]
            rows[i] += 1
            cols[j] += 1
            if rows[i] == n or cols[j] == m:
                return idx

        return 0


