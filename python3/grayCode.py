class Solution:
    def grayCode(self, n: int) -> List[int]:
        
        # need to generate integers that differ by 1 bit

        # what is f(i)?
        # 0 = 00
        # 1 = 01
        # 2 = 11
        # maybe right shift by 1 and xor i

        return [i >> 1 ^ i for i in range(2**n)]
        


        
