class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        
        cnt = sum(1 for i in s if i == '1')

        return (cnt - 1) * '1' + (len(s) - cnt) * '0' + '1'
            
        

