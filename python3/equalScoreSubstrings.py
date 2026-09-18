class Solution:
    def scoreBalance(self, s: str) -> bool:
        prefix = []
        for c in s:
            tmp = 0
            if len(prefix) > 0:
                tmp = prefix[-1]
            prefix.append(tmp + ord(c) - ord('a') + 1)
        
        suffix = 0
        for i, c in reversed(list(enumerate(s))):
            suffix += ord(c) - ord('a') + 1

            if i > 0 and suffix == prefix[i - 1]:
                return True

        return False
 
