class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        
        res = []
        for i in range(left, right + 1):

            tmp = i
            valid = True
            while tmp > 0:
                digit = tmp % 10
                
                if digit == 0 or i % digit != 0:
                    valid = False
                    break

                tmp //= 10

            if valid:
                res.append(i)
            
        return res


