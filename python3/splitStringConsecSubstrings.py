class Solution:
    def splitString(self, s: str) -> bool:

        n = len(s)

        def back(i, last):

            if int(s[i:]) == last - 1:
                return True
            
            res = []
            for j in range(i + 1, n):
                tmp = int(s[i:j])
                if tmp == last - 1:
                    res.append(back(j, tmp))

            return any(res)

        return any(back(i, int(s[:i])) for i in range(1, n))
