class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        # check if each element of nums1 is divisible by k * nums2
        # num1/(num2 * k) == n
        # num1/k == num2 * n 

        total = 0
        for i, x in enumerate(nums1):

            for j, y in enumerate(nums2):
                div = k * y
                if x % div == 0:
                    total += 1
        

        return total

