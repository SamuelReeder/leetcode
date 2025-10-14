class Solution:
    def smallestNumber(self, n: int) -> int:
        tmp = n
        mask = 1
        while tmp > 0:
            tmp //= 2
            mask = mask << 1

        return mask - 1
