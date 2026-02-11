class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        # trivial O(n^2)

        # sort and then have a sliding window 
        nums = sorted(nums)

        record = set()

        i, j = 0, 1
        while i < len(nums) - 1:
            if j == len(nums):
                i += 1
                j = i + 1
                continue 

            h = (nums[i], nums[j])
            tmp = abs(nums[j] - nums[i])
            if tmp == k and h not in record: 
                record.add(h)
                i += 1
                j = i + 1
            elif tmp < k:
                j += 1
            else:
                i += 1
                j = i + 1
        
        return len(record)

