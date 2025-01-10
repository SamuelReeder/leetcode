class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        longest = strs[0]
        for i in strs:
            for j in range(min(len(longest), len(i))):
                if longest[j] != i[j]:
                    longest = longest[:j]
                    break

            if len(longest) > len(i):
                longest = i

        return longest
