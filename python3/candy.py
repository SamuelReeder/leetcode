class Solution:
    def candy(self, ratings: List[int]) -> int:
        

        n = len(ratings)

        # checks with respect to left neighbor
        amounts = [1] * n
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                amounts[i] = amounts[i-1] + 1

        total = amounts[-1]
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1] and amounts[i] <= amounts[i + 1]:
                amounts[i] = amounts[i + 1] + 1
            total += amounts[i]

        return total

