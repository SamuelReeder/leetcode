class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        
        if n == 0:
            return 1
        
        res = 10
        digits = 9
        remaining = 9
        
        for i in range(2, n + 1):
            digits *= remaining
            res += digits
            remaining -= 1
            
        return res

