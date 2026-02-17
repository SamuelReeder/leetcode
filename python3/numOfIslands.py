class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        from collections import deque
        
        m, n = len(grid), len(grid[0])

        q = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    q.append((i, j))

        res = 0
        while q:
            q2 = deque()

            x, y = q.popleft()
            if grid[x][y] == "2":
                continue

            q2.append((x, y))
            another = False
            while q2:        
                
                i, j = q2.popleft()

                if grid[i][j] == "2":
                    continue

                another = True
                grid[i][j] = "2"
                adj = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]

                for k, l in adj:
                    if k >= m or k < 0 or l >= n or l < 0:
                        continue 

                    tmp = grid[k][l]
                    if tmp == "1":
                        q2.append((k, l))

            res += another
        
        return res



