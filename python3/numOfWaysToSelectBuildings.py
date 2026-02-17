class Solution:
    def numberOfWays(self, s: str) -> int:
        
        # need to select 3 buildings with no same consec buildings
        # 101 and 010
        # need to count num of prefixes for each indices, but only last is important

        n = len(s)

        n01 = 0
        n10 = 0

        n010 = 0
        n101 = 0

        zeros = 0
        ones = 0
        for i in range(n):

            if s[i] == "0":
                zeros += 1
                n10 += ones
                n010 += n01

            elif s[i] == "1":
                ones += 1
                n01 += zeros
                n101 += n10

        return n010 + n101          

