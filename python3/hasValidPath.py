class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        
        directions = {
            1: [(0, -1), (0, 1)],  # Street 1: Horizontal (left, right)
            2: [(1, 0), (-1, 0)],  # Street 2: Vertical (down, up)
            3: [(0, -1), (1, 0)],  # Street 3: Left-Down (left, down)
            4: [(0, 1), (1, 0)],   # Street 4: Right-Down (right, down)
            5: [(0, -1), (-1, 0)], # Street 5: Left-Up (left, up)
            6: [(0, 1), (-1, 0)]   # Street 6: Right-Up (right, up)
        }

        valid = {
            1: [{1, 4, 6}, {1, 3, 5}],  # Street 1: Valid connections for right and left
            2: [{2, 5, 6}, {2, 3, 4}],  # Street 2: Valid connections for down and up
            3: [{1, 4, 6}, {2, 5, 6}],  # Street 3: Valid connections for left and down
            4: [{1, 3, 5}, {2, 5, 6}],  # Street 4: Valid connections for right and down
            5: [{1, 4, 6}, {2, 3, 4}],  # Street 5: Valid connections for left and up
            6: [{1, 3, 5}, {2, 3, 4}]   # Street 6: Valid connections for right and up
        }

        m = len(grid)
        n = len(grid[0])

        visited = set()

        def dfs(point):
            visited.add(point)

            i, j = point
            c = grid[i][j]
            for k, d in enumerate(directions[c]):
                # 0,1
                y, x = d
                d_i, d_j = i + y, j + x
                if d_i < 0 or d_i >= m or d_j < 0 or d_j >= n:
                    continue

                if (d_i, d_j) in visited:
                    continue

                if grid[d_i][d_j] in valid[c][k]:
                    dfs((d_i, d_j))

        dfs((0, 0))
        
        return (m - 1, n - 1) in visited


















