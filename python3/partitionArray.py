class Solution:
    def partitionArray(self, nums: List[int], k: int) -> bool:
        
        n = len(nums)
        if n % k != 0:
            return False

        g = n // k
        hm = defaultdict(int)
        for num in nums:
            hm[num] += 1

            if hm[num] > g:
                return False

        return True
