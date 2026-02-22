class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        # we keep pointers
        # 0, 1, 2

        # first create pointers
        red = white = blue = 0
        for i in range(n):
            num = nums[i]
            if num == 0: # red
                tmp = nums[red]
                nums[red] = num
                red += 1
                num = tmp

            if num == 1: # white
                tmp = nums[white]
                nums[white] = num
                white += 1
                num = tmp
                
            if num == 2: # blue
                nums[blue] = num
                blue += 1

            white = max(red, white)
            blue = max(red, white, blue)

