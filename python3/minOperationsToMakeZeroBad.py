class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        # need to find min integer each time
        # can have a sorted set or a min heap
        # then will need to subtract from each element

        nums.sort()

        s = 0
        res = 0
        for i in nums:
            if i <= 0 or s >= i:
                continue
            s += (i - s)
            res += 1

        return res

        


            







        
