
iclass Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        
        if len(nums) == 0:
            return []
            
        res = []

        start = nums[0]
        last = nums[0]
        for i in nums[1:]:
            if i == last + 1:
                last = i
                continue

            if start == last:
                res.append(f"{start}")
            else:
                res.append(f"{start}->{last}")

            start = i
            last = i

        if start == last:
            res.append(f"{start}")
        else:
            res.append(f"{start}->{last}")

        return res
