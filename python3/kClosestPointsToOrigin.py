class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        import heapq

        heap = []

        for x, y in points:
            dist = sqrt(x**2 + y**2)
            heapq.heappush_max(heap, (dist, [x, y]))

            if len(heap) > k:
                heapq.heappop_max(heap)

        res = []
        for _ in range(k):
            res.append(heapq.heappop_max(heap)[1])

        return res
