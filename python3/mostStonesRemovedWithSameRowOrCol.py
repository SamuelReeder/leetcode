class Solution:
    def removeStones(self, stones: list[list[int]]) -> int:
        rows = defaultdict(list)
        cols = defaultdict(list) # indices of stones in col x or row y

        n = len(stones)
        for i, stone in enumerate(stones):
            cols[stone[0]].append(i)
            rows[stone[1]].append(i)

        # conduct bfs from each stone
        visited = set()
        c = 0
        for i, stone in enumerate(stones):
            # if member not visited, its a new components
            if i in visited:
                continue
            
            q = deque([i])
            c += 1

            while q:
                index = q.popleft()
                if index in visited:
                    continue
                visited.add(index)
                tmp = stones[index]

                for row_stone in rows[tmp[1]]:
                    q.append(row_stone)
                for col_stone in cols[tmp[0]]:
                    q.append(col_stone)

        return n - c     


