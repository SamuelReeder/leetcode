class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        

        i, j = 0, len(nums) - 1
        while i <= j:
            m = (i + j) // 2
            
            tmp = nums[m]
            if tmp == target:
                return True

            if nums[i] == tmp and nums[j] == tmp:
                j -= 1
                i += 1
            elif nums[i] <= tmp:
                if nums[i] <= target < tmp:
                    j = m - 1
                else:
                    i = m + 1
            else:
                if tmp < target <= nums[j]:
                    i = m + 1
                else:
                    j = m - 1

        return False
