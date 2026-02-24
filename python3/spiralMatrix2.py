class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:        
        res = [[0 for _ in range(n)] for _ in range(n)]

        dx, dy = 1, 0
        i = j = 0
        curr = 1
        while curr <= n**2:
            if not (0 <= i < n and 0 <= j < n) or res[i][j] > 0:
                i -= dy
                j -= dx
                dx, dy = -dy, dx
            else:
                res[i][j] = curr
                curr += 1
            
            i += dy
            j += dx

        # for r in res:
        #     print("\n", r)

        return res


