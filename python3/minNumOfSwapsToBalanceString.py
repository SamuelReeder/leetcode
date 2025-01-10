class Solution:
    def minSwaps(self, s: str) -> int:
        if not s: return 0

        imbalance = 0
        max_imbalance = 0

        for char in s:
            if char == '[':
                imbalance += 1
            elif char == ']':
                imbalance -= 1

            max_imbalance = min(max_imbalance, imbalance)

        return (-max_imbalance + 1) // 2
