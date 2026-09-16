class Solution:
    def minimumSwaps(self, nums: list[int]) -> int:
        r = len(nums) - 1
        res = l = 0
        while l < r:
            if nums[l] != 0:
                l += 1
            elif nums[r] == 0:
                r -= 1
            else:
                l += 1
                r -= 1
                res += 1
        return res

        return res


