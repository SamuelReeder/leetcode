class Solution:
    def mySqrt(self, x: int) -> int:
        
        if x < 2:
            return x
        
        left, right = 1, (x // 2)

        while left <= right:
            m = (left + right) // 2

            tmp = m * m
            if tmp == x:
                return m
            elif tmp < x:
                left = m + 1
            else:
                right = m - 1
        
        return right
            



