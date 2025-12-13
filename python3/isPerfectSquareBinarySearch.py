class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        
        if num < 2:
            return True

        l = 2
        h = num // 2
        while l <= h:
            m = ((h - l) // 2) + l
            if m * m == num:
                return True
            elif m * m < num:
                l = m + 1
            else:
                h = m - 1
        
        return False

