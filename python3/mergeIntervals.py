class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        # just sort?
        
        intervals = sorted(intervals)

        res = []
        start, end = intervals[0]
        for s, e in intervals[1:]:
            if s <= end and e > end:
                end = e
            elif s > end:
                res.append([start, end])
                start, end = s, e
        
        res.append([start, end])

        return res


