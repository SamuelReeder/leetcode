class Solution:
    def unmarkedSumArray(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        # priority queue sorted by value then index

        mark = [False] * len(nums)

        import heapq

        min_heap = []
        for i, num in enumerate(nums):
            heapq.heappush(min_heap, (num, i))
        
        total = sum(nums)
        ans = []
        for idx, k in queries:
        
            if not mark[idx]:
                total -= nums[idx]
                mark[idx] = True

            while min_heap and k > 0:
                val, i = heapq.heappop(min_heap)
                if not mark[i]:
                    k -= 1
                    total -= val
                    mark[i] = True

            ans.append(total)

        return ans






