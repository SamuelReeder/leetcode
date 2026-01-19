class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        res, neg = 0, 0
        minimum = 10**5 + 1

        for row in matrix:
            for col in row:
                res += abs(col)
                if col < 0:
                    neg += 1
                minimum = min(minimum, abs(col))

        if neg % 2 != 0:
            res -= 2 * minimum

        return res
