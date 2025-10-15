class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        
        n = len(words)

        res = []
        last = None
        for i in range(n):
            if groups[i] != last:
                last = groups[i]
                res.append(words[i])

        return res
