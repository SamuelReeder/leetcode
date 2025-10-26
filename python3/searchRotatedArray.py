class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        # binary search
        # split array in half
        # the rotation can either be at center, or in one of the halfs
        # take range of each half
        # if start < end, its normal
        # if end < start its rotated

        n = len(nums)
        i = 0
        j = n - 1
        
        while i <= j:
            m = (i + j) // 2
            
            if nums[m] == target:
                return m
                        
            if nums[i] <= nums[m]:
                if nums[i] <= target < nums[m]:
                    j = m - 1
                else:
                    i = m + 1
            else:
                if nums[m] < target <= nums[j]:
                    i = m + 1
                else:
                    j = m - 1
                    
        return -1

