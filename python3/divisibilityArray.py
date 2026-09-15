class Solution:
    def divisibilityArray(self, word: str, m: int) -> List[int]:

        n = len(word)
        div = [0] * n

        prefix = 0
        
        remainder = 0
        for i, w in enumerate(word):
            remainder = (remainder * 10 + int(w)) % m
            if remainder == 0:
                div[i] = 1

        return div






        
