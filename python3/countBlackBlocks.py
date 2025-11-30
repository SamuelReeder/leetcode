class Solution:
    def countBlackBlocks(self, m: int, n: int, coordinates: List[List[int]]) -> List[int]:
        
        arr = [0] * 5

        from collections import defaultdict
        tmp = defaultdict(int)

        for x, y in coordinates:
            # we map blocks by top left
            potential_blocks = [
                (x, y),
                (x - 1, y),
                (x, y - 1),
                (x - 1, y - 1)
            ]

            for a, b in potential_blocks:
                if 0 <= a < m - 1 and 0 <= b < n - 1:
                    tmp[(a, b)] += 1

        for count in tmp.values():
            arr[count] += 1
            
        arr[0] = (m - 1) * (n - 1) - sum(arr[1:])

        return arr


