class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # 2, 3, 1
        # 3, 1, 2
        # maybe we take last correctly sorted element and swap
        # how to find last correctly sorted:
        # - ascending
        # 4325413 becomes 4325431
        # 432531 needs to be 433125

        def reverse(start):
            i, j = start, len(nums) - 1
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1

        last = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < last:
                # when we get here we need the smallest num to the right nums[i] thats greater than nums[i]
                # maybe we can sort and bisect

                # TODO: can improve this by just reversing the array, since they were reverse sorted before
                reverse(i + 1)
                # g is index of first element greater than than nums[i] in nums[i + 1:]
                g = bisect.bisect_right(nums[i + 1:], nums[i]) + i + 1
                nums[i], nums[g] = nums[g], nums[i]
                return nums

            last = nums[i]

        return nums.reverse()


        
