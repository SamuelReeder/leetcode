oclass Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        n = len(bottomLeft)

        # interset if bottom right is < top left of another (both indices)
        # for every bottom left and top right
        maximum = 0
        for i in range(n):
            for j in range(i + 1, n):

                # check that bottom right of one rectangle is less than top left of another
                # and that the top left of first rectangle is greater than bottom right of another
                a_i, b_i = bottomLeft[i]
                c_i, d_i = topRight[i]

                a_j, b_j = bottomLeft[j]
                c_j, d_j = topRight[j]

                left = max(a_i, a_j)
                right = min(c_i, c_j)

                top = min(d_i, d_j)
                bottom = max(b_i, b_j)

                if right - left > 0 and top - bottom > 0:
                    maximum = max(maximum, min(right - left, top - bottom))

        return maximum**2 




        




