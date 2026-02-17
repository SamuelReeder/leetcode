class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        

        n = len(nums)
        first_neg, last_neg = None, None
        product = 1
        start = None
        maximum = 0
        for i in range(n):

            if nums[i] == 0:
                # compute length of last subarray
                if start is None:
                    continue

                if product > 0:
                    maximum = max(maximum, i - start)
                else:
                    prefix = first_neg + 1
                    tmp = max(last_neg - start, i - prefix)
                    maximum = max(maximum, tmp)

                first_neg, last_neg = None, None
                product = 1
                start = None    
                continue               

            if start is None:
                start = i

            product *= 1 if nums[i] > 0 else -1

            if nums[i] > 0:
                continue

            if first_neg is None:
                first_neg = i
            
            last_neg = i

        if start is None:
            return maximum 

        if product > 0:
            maximum = max(maximum, n - start)
        else:
            prefix = first_neg + 1
            tmp = max(last_neg - start, n - prefix)
            maximum = max(maximum, tmp)
            
        return maximum






        

