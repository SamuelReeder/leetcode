class Solution:
    def myPow(self, x: float, n: int) -> float:
        # x times itself n times
        if abs(n) <= 2:
            if n < 0:
                x = 1 / x
            
            n = abs(n)
            if n == 2:
                return x * x
            if n == 1:
                return x
            if n == 0:
                return 1 

        half = self.myPow(x, n // 2)
        res = 1 if n % 2 == 0 else x
            
        return res * half * half
            

        
