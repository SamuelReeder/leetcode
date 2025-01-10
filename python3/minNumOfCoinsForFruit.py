class Solution:
    def minimumCoins(self, prices: List[int]) -> int:
        n = len(prices)
        d = [float('inf')] * n  # minimum price to acquire all up to the ith fruit 

        for i in range(n - 1, -1, -1):
            if i + i + 1 >= n - 1:
                d[i] = prices[i]
                continue
            for j in range(i + 1, min(i + 3 + i, n)):
                d[i] = min(d[i], d[j] + prices[i])
        
        print(d)
        return d[0]

        
