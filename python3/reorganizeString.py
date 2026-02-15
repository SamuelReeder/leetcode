class Solution:
    def reorganizeString(self, s: str) -> str:
        
        from collections import Counter
        hm = Counter(s)

        import heapq

        max_heap = [(v, k) for k, v in hm.items()]
        heapq.heapify_max(max_heap)

        s = ""
        while len(max_heap) > 0:

            count, c = heapq.heappop_max(max_heap)
            tmp = []
            while len(s) > 0 and s[-1] == c and len(max_heap) > 0:
                tmp.append((count, c))
                count, c = heapq.heappop_max(max_heap)

            if len(s) > 0 and s[-1] == c:
                return ""

            s += c
            if count > 1:
                tmp.append((count - 1, c))

            for i in tmp:
                heapq.heappush_max(max_heap, i)
        
        return s

            






