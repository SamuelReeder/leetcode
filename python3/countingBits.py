class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0]

        # have a count which starts at 0
        # we basically add binary 1 each time
        # a simplification is if its odd 1 and if even 0

        curr = 0

        p = 0
        for i in range(1, n + 1):
            if 2**p == i:
                ans.append(1)
                p += 1
            else:
                tmp = 2**(p - 1)
                ans.append(ans[i - tmp] + 1)

        return ans
