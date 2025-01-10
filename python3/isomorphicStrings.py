class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        n = len(s)
        mapping = {}
        mapp = {}

        for i in range(n):
            if (s[i] in mapping and mapping[s[i]] != t[i]) or (t[i] in mapp and mapp[t[i]] != s[i]):
                return False
            mapping[s[i]] = t[i]
            mapp[t[i]] = s[i]
        
        return True

