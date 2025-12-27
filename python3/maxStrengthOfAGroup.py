class Solution:
    def maxStrength(self, nums: List[int]) -> int:
        
        max_neg = 1
        max_pos = 1
        for num in nums:
            max_neg, max_pos = min(max_neg * num, max_pos * num, max_neg), max(max_pos * num, max_neg * num, max_pos)

        if max_pos == 1:
            cnt = 0
            m = None
            for num in nums:
                if m is None or num > m:
                    m = num
                if num < 0:
                    cnt += 1

            if cnt < 2:
                return m

        return max_pos
