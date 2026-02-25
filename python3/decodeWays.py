class Solution: 
    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0

        dp = [0] * len(s)
        dp[0] = 1
        for i in range(1, len(s)):
            first, second = int(s[i - 1]), int(s[i])

            num = first * 10 + second
            if not 1 <= first <= 2 and second == 0:
                return 0

            if second != 0:
                dp[i] += dp[i - 1]

            if 10 <= num <= 26:
                dp[i] += dp[i - 2] if i > 1 else 1

        return dp[-1]

