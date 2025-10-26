class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        # hash set to find a
        # subtract from sum to find b

        seen = set()
        a = None
        s = 0
        for row in grid:
           for col in row:
                if col in seen:
                    a = col
                else:
                    seen.add(col)
                    s += col
        
        n_square = len(grid)**2
        return [a, n_square * (n_square + 1) // 2 - s]
        
