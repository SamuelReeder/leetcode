class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        # when we find a 1, do a bfs to add all elements of the island to a set

        from collections import deque

        n = len(grid)
        q = deque()

        found = False
        range_n = range(n)
        for i in range_n:
            for j in range_n:
                if grid[i][j] == 1:
                    q.append((i, j))
                    grid[i][j] = 2
                    found = True
                    break
            if found: break

        q_final = deque()
        while q:
            i, j = q.popleft()

            q_final.append((i, j))
            close = [(i, j + 1), (i + 1, j), (i, j - 1), (i - 1, j)]
            for k, l in close:
                if k in range_n and l in range_n and grid[k][l] == 1:
                    grid[k][l] = 2
                    q.append((k, l))
                    
        res = 0
        tmp_q = deque()
        while q_final:
            while q_final:
                i, j = q_final.popleft()

                close = [(i, j + 1), (i + 1, j), (i, j - 1), (i - 1, j)]
                for k, l in close:
                    if k not in range_n or l not in range_n:
                        continue
                    
                    if grid[k][l] == 0:
                        grid[k][l] = 3
                        tmp_q.append((k, l))
                    elif grid[k][l] == 1:
                        return res
            
            res += 1
            q_final = tmp_q
            tmp_q = deque()

        return res

            



                


        
