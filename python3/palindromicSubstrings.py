class Solution:
    def countSubstrings(self, s: str) -> int:
        # for each index i we check for palindromes centered at it

        n = len(s)
        res = n
        for i in range(1, n):
            
            j = i + 1
            k = i - 1
            while j < n and k >= 0 and s[j] == s[k]:
                res += 1
                j += 1
                k -= 1

            j = i
            k = i - 1
            while j < n and k >= 0 and s[j] == s[k]:
                res += 1
                j += 1
                k -= 1

        return res


            


