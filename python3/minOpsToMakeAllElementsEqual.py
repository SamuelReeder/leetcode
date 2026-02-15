class Solution:
    def minOperations(self, nums: List[int], queries: List[int]) -> List[int]:
        
        nums.sort()
        n = len(nums)
        
        p_sum = [0] * (n + 1) 
        for i in range(n):
            p_sum[i + 1] = nums[i] + p_sum[i]

        def binary_search(q):
            i, j = 0, n
            while i < j:
                m = (j + i) // 2
                if nums[m] < q:
                    i = m + 1
                else:
                    j = m

            return i

        answer = []
        for q in queries:
            i = binary_search(q)

            # i is the element that is less than q
            res = (q * i) - p_sum[i]
            res += (p_sum[-1] - p_sum[i]) - (q * (n - i))

            answer.append(res)

        return answer
