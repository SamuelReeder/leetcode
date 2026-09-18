class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        
        def reverse(x: int) -> int:
            res = 0
            while x > 0:
                r = x % 10
                res = res * 10 + r
                x //= 10
            return res

        rev = [reverse(num) for num in nums]
        
        mi = float("inf")
        hm = {}
        for j, num in enumerate(nums):
            if num in hm:
                mi = min(mi, abs(hm[num] - j))
            hm[rev[j]] = j
        
        if mi == float("inf"):
            return -1
        return mi

            
            

