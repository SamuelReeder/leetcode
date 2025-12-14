class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:

        def prime(num) -> bool:
            if num <= 1:
                return False

            for i in range(2, int(num**0.5) + 1):
                if num % i == 0:
                    return False
            
            return True

        if all(x < y for x, y in zip(nums, nums[1:])):
            return True

        last = 0
        for i in range(len(nums)):
            tmp = nums[i] - last - 1

            p = None
            while tmp > 0:
                if prime(tmp):
                    p = tmp
                    break
                tmp -= 1

            if p is None and nums[i] <= last:
                return False
            elif p is not None:
                nums[i] -= p
            
            last = nums[i]

        return True

            




