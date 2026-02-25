class Solution:
    def countAndSay(self, n: int) -> str:
        
        if n == 1:
            return "1"

        s = self.countAndSay(n - 1)
        res = ""
        cnt = 1
        for i in range(1, len(s)):
            if s[i] != s[i - 1]:
                res += str(cnt) + s[i - 1]
                cnt = 1
            else:
                cnt += 1

        res += str(cnt) + s[-1]
        return res
