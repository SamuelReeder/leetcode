class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        # bfs

        q = deque()
        q.append((sr, sc))
        starting = image[sr][sc]

        while q:
            r, c = q.pop()
            if image[r][c] == color:
                continue

            image[r][c] = color
            adj = [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]
            for i, j in adj:
                if not 0 <= i < len(image) or not 0 <= j < len(image[0]):
                    continue

                if image[i][j] == starting:
                    q.append((i, j))

        return image
                


