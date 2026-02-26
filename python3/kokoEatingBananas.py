class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # you want to look for minimum integer s.t. all piles can be eaten

        left, right = 1, max(piles)
        while left < right:
            mid = (left + right) // 2
            if sum(math.ceil(pile / mid) for pile in piles) <= h:
                right = mid
            else:
                left = mid + 1
        return left
