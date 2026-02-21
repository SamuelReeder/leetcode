class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        # cases:
        # nums[m] is target then the range is wrapped around
        # nums[m] < target then its higher
        # nums[m] > target then its lower
        
        left = right = -1
        def helper(is_left):
            nonlocal left, right
            i, j = 0, len(nums) - 1

            while i <= j:
                m = (i + j) // 2
                if nums[m] == target:
                    if is_left:
                        j = m - 1
                        left = m
                    else:
                        i = m + 1
                        right = m
                elif nums[m] < target:
                    i = m + 1
                elif nums[m] > target:
                    j = m - 1
            
        helper(True)
        helper(False)

        return [left, right]

