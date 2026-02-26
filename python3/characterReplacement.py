class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freqs = defaultdict(int)
        res = i = 0

        for j in range(len(s)):
            freqs[s[j]] += 1
            ma = max(freqs.values())
            curLen = j - i + 1
            if curLen - ma > k: # window cant be all one letter
                freqs[s[i]] -= 1
                i += 1
            res = max(res, j - i + 1)
        
        return res
