class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        
        n = len(nums)
        
        diff = [0] * (2 * limit + 2)
        for i in range(n // 2):
            first = nums[i]
            second = nums[n - 1 - i]
            maximum = max(first, second)
            minimum = min(first, second)

            diff[minimum + 1] -= 1
            diff[maximum + limit + 1] += 1

            diff[first + second] -= 1
            diff[first + second + 1] += 1

            
        m = 10**5 + 1
        cnt = n
        for i in diff:
            n += i
            m = min(m, n)

        return m

        

