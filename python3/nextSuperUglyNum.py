class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        
        
        nums = [1]

        cnt = [0] * len(primes)

        for _ in range(1, n):

            minimum, final = 2**31 - 1, None
            for i in range(0, len(cnt)):
                
                tmp = nums[cnt[i]] * primes[i]
                if tmp < minimum and tmp <= nums[-1]:
                    cnt[i] += 1
                    tmp = nums[cnt[i]] * primes[i]

                if tmp < minimum:
                    minimum = tmp
                    final = i

            nums.append(minimum)
            cnt[final] += 1

        return nums[-1]


                
                

        

                



                

