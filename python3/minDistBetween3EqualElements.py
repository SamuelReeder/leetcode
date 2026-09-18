class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        # good: nums[i] == nums[j] == nums[k]
        # dist: abs(i - j) + abs(j - k) + abs(k - i)
        # let x < y < z be the min, middle, and max of i, j, k respectively
        # dist = (y - x) + (z - y) + (z - x) = 2z - 2x = 2(z - x) = 2(max - min) 

        # group by numbers
        indices = defaultdict(list)
        for num in enumerate(nums):
            # every list is sorted by index already
            indices[num[1]].append(num[0])

        res = float("inf")
        for v in indices.values():
            if len(v) <= 2:
                continue
            for i in range(len(v) - 2):
                res = min(res, 2 * (v[i + 2] - v[i]))

        if res == float("inf"):
            return -1
        return res
            

