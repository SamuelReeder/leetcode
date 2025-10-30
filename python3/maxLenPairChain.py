class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        # looking for lowest b and lowest c

        # make one array sorted by c

        s_pairs = sorted(pairs, key=lambda x: (x[1], -x[0]))

        last = s_pairs[0][1]
        res = 1
        for pair in s_pairs[1:]:
            if last < pair[0]:
                last = pair[1]
                res += 1
            
        return res



