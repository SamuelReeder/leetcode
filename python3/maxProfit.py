class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        m = 0
        for p in prices:
            if p < buy:
                buy = p
            m = max(m, p - buy)
        return m



