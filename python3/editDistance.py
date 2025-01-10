class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        n, m = len(word1), len(word2)

        # ed[i][j] is min distance to convert word1[:i] to word2[:j]
        ed = [[0] * (m + 1) for _ in range(n + 1)]

        for i in range(n + 1):
            ed[i][0] = i
        
        for i in range(m + 1):
            ed[0][i] = i

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                ins = ed[i-1][j] + 1  
                d = ed[i][j-1] + 1
                ed[i][j] = min(ins, d, ed[i-1][j-1] if word1[i - 1] == word2[j - 1] else ed[i-1][j-1] + 1)
        
        return ed[n][m]
        
