class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        def helper(seen, arr):
            # we need to generate each ordering of elements in the array
            # we start with default array. with the default array, we switch each possible element with one another
            # then we recurse and do the same
            # but how to avoid duplicates?
            # keep a set

            if len(arr) == len(nums):
                res.append(list(arr))
                return

            for i in range(len(nums)):
                # we need to add element i and ensure it isnt added again
                if i in seen:
                    continue
                arr.append(nums[i])
                seen.add(i)
                helper(seen, arr)
                arr.pop()
                seen.remove(i)


        helper(set(), [])

        return res
