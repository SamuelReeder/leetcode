class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        
        minimum = 10**5
        for i, v in enumerate(nums):
            if v != target:
                continue

            minimum = min(minimum, abs(i - start))

        return minimum
