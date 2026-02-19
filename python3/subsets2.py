class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        nums.sort()

        res = []
        seen = set()

        n = len(nums)

        def helper(i, sub):
            
            if i == len(nums):
                tmp = tuple(sub)
                if tmp not in seen:
                    res.append(list(sub))
                    seen.add(tmp)
                return
            
            sub.append(nums[i])
            helper(i + 1, sub)

            sub.pop()
            helper(i + 1, sub)

        s = []
        helper(0, s)

        return res


