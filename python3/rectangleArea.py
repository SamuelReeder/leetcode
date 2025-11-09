oclass Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:

        one = (ax2 - ax1) * (ay2 - ay1)
        two = (bx2 - bx1) * (by2 - by1)

        area = one + two

        top = min(ay2, by2)
        bottom = max(ay1, by1)

        right = min(ax2, bx2)
        left = max(ax1, bx1)
        
        height = top - bottom
        width = right - left

        if height > 0 and width > 0:
            area -= height * width

        return area
        
