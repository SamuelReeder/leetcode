class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        from collections import deque

        q = deque()

        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i, j))

        # need to track minutes too
        # in other words, depth of bfs

        level = 0
        while q:
            tmp = deque()

            while q:

                curr = q.popleft()
                i, j = curr
                neighbors = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]
                for k, l in neighbors:
                    if k < 0 or k >= m or l < 0 or l >= n:
                        continue
                    idx = (k, l)
                    if grid[k][l] not in [2, 0]:
                        tmp.append(idx)
                        grid[k][l] = 2
            q = tmp

            level += bool(q)

        for row in grid:
            if 1 in row:
                return -1

        return level


        
