class Solution:
    def minSwaps(self, grid: list[list[int]]) -> int:
        n = len(grid)
        max_one = [-1] * n
        for i, row in enumerate(grid):
            for j in range(len(row) - 1, -1, -1):
                if row[j] == 1:
                    max_one[i] = j
                    break

        if any(x > i for i, x in enumerate(sorted(max_one))):
            return -1

        res = 0
        for i in range(n - 1):
            if max_one[i] <= i:
                continue
            tmp = max_one[i]
            swap = i + 1
            for j in range(i + 1, n):
                if max_one[j] <= i:
                    swap = j
                    break
                max_one[j], tmp = tmp, max_one[j]

            max_one[i], max_one[swap] = max_one[swap], tmp
            res += abs(i - swap)

        return res

             





