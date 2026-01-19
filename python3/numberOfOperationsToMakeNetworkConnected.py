class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        
        m = len(connections)
        if m < n - 1:
            return -1

        adj = [[] for _ in range(n)]
        for a, b in connections:
            adj[a].append(b)
            adj[b].append(a)

        seen = set()
        def dfs(node):
            if node in seen:
                return

            seen.add(node)

            start = len(seen)
            for a in adj[node]:
                dfs(a)

        res = 0
        for i in range(n):
            if i not in seen:
                res += 1
                dfs(i)

        return res - 1
             



        

