class Solution:
    def knightDialer(self, n: int) -> int:
        
        moves = {
            0: [4, 6],
            1: [6, 8],
            2: [7, 9],
            3: [4, 8],
            4: [3, 9, 0],
            5: [],
            6: [1, 7, 0],
            7: [2, 6],
            8: [1, 3],
            9: [2, 4]
        }

        # dp[i] is the number of sequences of n - 1 from i where n - 1 is implicit from n - 2 version
        dp = [1 for _ in range(10)]

        for _ in range(1, n):
            tmp = [0] * 10
            for i in range(10):
                for move in moves[i]:
                    tmp[i] = (tmp[i] + dp[move]) % (10**9 + 7)
            dp = tmp
        
        return sum(dp) % (10**9 + 7)

