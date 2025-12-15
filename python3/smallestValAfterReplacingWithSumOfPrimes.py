class Solution:
    def smallestValue(self, n: int) -> int:
        
        
        m = math.inf
        while True:

            tmp = n
            s = 0
            i = 2
            while i * i <= n:
                if n % i == 0:
                    s += i
                    n //= i
                else:
                    i += 1
            
            if n > 1:
                s += n
                
            m = min(m, s)
            n = s

            if n == tmp:
                break
        
        return m



            
            
        

            


