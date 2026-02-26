class Solution:
    def numTrees(self, n: int) -> int:
        
        seen = dict()
        def helper(start, end):
            if start >= end:
                return 1

            if (start, end) in seen:
                return seen[(start,end)]

            total = 0
            for i in range(start, end + 1):
                total += (helper(start, i - 1) * helper(i + 1, end))

            seen[(start,end)] = total
            return total

        return helper(1, n)
             
