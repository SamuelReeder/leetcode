class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def palindrome(sub):
            return sub == sub[::-1]

        res = []
        def backtrack(start, parts):
            if start == len(s):
                res.append(list(parts))
                return
            for i in range(start + 1, len(s) + 1):
                if palindrome(s[start:i]):
                    parts.append(s[start:i])
                    backtrack(i, parts)
                    parts.pop()

        backtrack(0, [])
        return res
