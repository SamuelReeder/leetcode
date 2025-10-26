class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        
        # remove intervals contained in some other interval
        # could sort list?

        s = sorted(intervals)

        res = 0
        highest = -1
        for i in range(len(s)):
            if highest != -1 and highest >= s[i][1]:
                res += 1
            elif i + 1 < len(s) and s[i][0] == s[i+1][0]:
                res += 1
            
            highest = max(highest, s[i][1])

        return len(intervals) - res
