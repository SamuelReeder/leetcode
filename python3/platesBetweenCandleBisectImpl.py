class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        prefix = [0] * len(s)
        bars = []
        for i in range(len(s)):
            if s[i] == "|":
                bars.append(i)
                prefix[i] = prefix[i - 1]
            else:
                prefix[i] = prefix[i - 1] + 1

        answer = []
        for left, right in queries:
            l = bisect.bisect_left(bars, left)
            r = bisect.bisect_right(bars, right) - 1

            if l >= r or bars[l] >= bars[r]:
                answer.append(0)
            else:
                answer.append(prefix[bars[r]] - prefix[bars[l]])

        return answer
