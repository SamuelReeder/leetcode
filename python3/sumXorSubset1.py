class Solution:

    @staticmethod
    def xor(arr):
        xor = 0
        for i in arr:
            xor ^= i
        return xor

    @staticmethod
    def helper(i, arr, subset):
        
        if i == len(arr):
            return Solution.xor(subset)

        total = 0

        subset.append(arr[i])
        total += Solution.helper(i + 1, arr, subset)
        
        subset.pop()
        total += Solution.helper(i + 1, arr, subset)

        return total

    def subsetXORSum(self, nums: List[int]) -> int:
        
        res = []
        subset = []
        return Solution.helper(0, nums, subset)            

