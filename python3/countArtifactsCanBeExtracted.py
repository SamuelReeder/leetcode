
class Solution:
    def digArtifacts(self, n: int, artifacts: List[List[int]], dig: List[List[int]]) -> int:
        

        grid = [[False for _ in range(n)] for _ in range(n)]

        for r, c in dig:
            grid[r][c] = True

        res = 0
        for r1, c1, r2, c2 in artifacts:

            exc = True
            
            for i in range(r1, r2 + 1):

                for j in range(c1, c2 + 1):

                    if not grid[i][j]:
                        exc = False
                        break
            
            if exc:
                res += 1

        return res
