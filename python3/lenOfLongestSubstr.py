class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # two cases:
        # - the next character is a duplicate, we reduce the size of the curr string
        # - not duplicate, we remain the same=
        # need to track dups

        seen = dict()
        longest = curr = start = 0
        for i in range(len(s)):
            c = s[i]
            if c not in seen or seen[c] < start:
                curr += 1
                longest = max(curr, longest)
                seen[c] = i
            else:
                curr -= (seen[c] - start)
                start = seen[c] + 1
                seen[c] = i
        
        return longest

