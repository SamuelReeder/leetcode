# messy solution

class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        
        verticalCuts = sorted(verticalCuts)
        horizontalCuts = sorted(horizontalCuts)

        vert = verticalCuts[0]
        for i in range(1, len(verticalCuts)):
            cut = verticalCuts[i] - verticalCuts[i - 1]
            vert = max(vert, cut)

        vert = max(vert, w - verticalCuts[-1])

        hor = horizontalCuts[0]
        for i in range(1, len(horizontalCuts)):
            cut = horizontalCuts[i] - horizontalCuts[i - 1]
            hor = max(hor, cut)

        hor = max(hor, h - horizontalCuts[-1])

        return (hor * vert) % (10**9 + 7)


