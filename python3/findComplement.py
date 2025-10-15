class Solution:
    def findComplement(self, num: int) -> int:
        
        amount = 0
        while num >> amount > 0:
            amount += 1
        
        return (~num) & (2**amount - 1)
