class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        
        cnt = 0
        # can also do xor and check for 1s
        m = max(x, y)
        while m > 0:
            if x & 1 != y & 1:
                cnt += 1

            x >>= 1
            y >>= 1
            m >>= 1

        return cnt
