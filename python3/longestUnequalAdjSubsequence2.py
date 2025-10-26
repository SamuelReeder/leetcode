class Solution:
    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
    
        def hamming(word1: str, word2: str):
            count = 0
            for i in range(len(word1)):
                if word1[i] != word2[i]:
                    count += 1
            return count 

        n = len(words)

        # dp[i] is the len of the longest subsequence ending at words[i]
        dp = [1] * n
        # the value of words[i] (or lower), can determine if words[i+1] can be added

        # subsequence = [[] for _ in range(n)]
        subsequence = [-1] * n
        final = 1
        index = 0
        for i in range(1, n):

            for j in range(0, i):
                
                if groups[i] != groups[j] and len(words[i]) == len(words[j]) and hamming(words[i], words[j]) == 1:
                    dp[i] = max(dp[j] + 1, dp[i])
                    if dp[i] == dp[j] + 1:
                        subsequence[i] = j

            if dp[i] > final:
                final = dp[i]
                index = i

        from collections import deque

        ls = deque([words[index]])
        
        while True:
            curr = subsequence[index]
            if curr == -1:
                break
            
            ls.appendleft(words[curr])
            index = curr

        return list(ls)




        
