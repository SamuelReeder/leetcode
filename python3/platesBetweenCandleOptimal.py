class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:

        cnt = [0] * len(s)
        prefix = [0] * len(s)
        suffix = [0] * len(s)

        idx = None
        for i in range(len(s)):
            if s[i] == "|":
                idx = i
                cnt[i] = cnt[i - 1]
            else:
                cnt[i] = cnt[i - 1] + 1
                
            prefix[i] = idx
            

        idx = None
        for i in range(len(s) - 1, -1, -1):
            if s[i] == "|":
                idx = i
            suffix[i] = idx

        answer = []
        for left, right in queries:
            r_bound = prefix[right]
            l_bound = suffix[left]

            if r_bound is None or l_bound is None or r_bound <= l_bound:
                answer.append(0)
            else:
                answer.append(cnt[r_bound] - cnt[l_bound])
            
        print(cnt)
        print(prefix)
        print(suffix)
        return answer
