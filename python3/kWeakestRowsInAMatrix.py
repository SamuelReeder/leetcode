class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        
        # need count of soldiers in each row
        # then order by least soldiers and indices
        sums = [(sum(row), i) for i, row in enumerate(mat)]
        return [i for row, i in sorted(sums)[:k]]

