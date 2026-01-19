class Solution:
    def countTexts(self, pressedKeys: str) -> int:

        MOD = 10**9 + 7
        n = len(pressedKeys)

        hm = {'2': 3, '3': 3, '4': 3, '5': 3, '6': 3, '7': 4, '8': 3, '9': 4}
        sequences = {3: [1, 1, 2, 4], 4: [1, 1, 2, 4]}

        for i in range(4, n + 1):
            sequences[3].append((sequences[3][i - 1] + sequences[3][i - 2] + sequences[3][i - 3]) % MOD)
            sequences[4].append((sequences[4][i - 1] + sequences[4][i - 2] + sequences[4][i - 3] + sequences[4][i - 4]) % MOD)
        
        cnt = 0
        res = 1
        for i in range(1, n):
            cnt += 1
            if pressedKeys[i] != pressedKeys[i - 1]:
                res = (res * sequences[hm[pressedKeys[i - 1]]][cnt]) % MOD
                cnt = 0
            
        return (res * sequences[hm[pressedKeys[-1]]][cnt + 1]) % MOD

