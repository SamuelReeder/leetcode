class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        
        primes={2, 3,5,7,11,13,17,19,23,29,31}

        def set_bits(num: int) -> int:
            cnt = 0
            while num > 0:
                cnt += num & 1
                num >>= 1

            return cnt

        res = 0
        for i in range(left, right + 1):
            res += set_bits(i) in primes

        return res


