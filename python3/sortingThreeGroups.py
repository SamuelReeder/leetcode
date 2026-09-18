class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        cnt = {1: 0, 2: 0, 3: 0}

        for num in nums:
            tmp = max(cnt[i] + 1 for i in range(1, num + 1))
            cnt[num] = max(tmp, cnt[num])

        return len(nums) - max(cnt.values()) 

