class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        res = []

        def helper(arr, hm):
            if len(arr) == len(nums):
                res.append(list(arr))
                return

            
            for k, v in hm.items():
                if v > 0:

                    hm[k] -= 1
                    arr.append(k)
                    helper(arr, hm)
                    arr.pop()
                    hm[k] += 1


        d = dict()
        for i in nums:
            if i not in d:
                d[i] = 1
                continue
            d[i] += 1

        helper([], d)

        return res
