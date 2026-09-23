class Solution:
    def minimumPartition(self, s: str, k: int) -> int:
        arr = [int(c) for c in s]
        curr = res = 0
        for i in arr:
            if i > k:
                return -1

            tmp = curr * 10 + i
            if tmp <= k:
                curr = tmp
            else:
                res += 1
                curr = i
        return res + 1
