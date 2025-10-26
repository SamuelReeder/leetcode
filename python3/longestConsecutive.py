class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        # have a set of elements
        # loop if its start of set

        s = set(nums)
        res = 0
        for num in s:

            if num - 1 in s:
                continue

            i = num + 1
            while i in s:
                i += 1

            res = max(res, i - num)

        return res
