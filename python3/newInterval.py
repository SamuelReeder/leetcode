class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        i = bisect.bisect_left(intervals, newInterval)

        res = intervals[:i]
        start, end = newInterval
        if i > 0 and intervals[i - 1][1] >= start:
            start = intervals[i - 1][0]
            end = max(intervals[i-1][1], end)
            res.pop()

        while i < len(intervals) and intervals[i][0] <= end:
            end = max(end, intervals[i][1])
            i += 1
        
        res.append([start,end]) 
        return res + intervals[i:]
