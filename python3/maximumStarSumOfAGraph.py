class Solution:
    def maxStarSum(self, vals: list[int], edges: list[list[int]], k: int) -> int:
        n = len(vals)
        adj = defaultdict(set)
        for u, v in edges:
            if vals[v] > 0:
                adj[u].add(v)
            if vals[u] > 0:
                adj[v].add(u)

        res = -10**5
        for i, val in enumerate(vals):
            top_k = sorted(adj[i], reverse=True, key=lambda x:vals[x]) if len(adj[i]) > k else list(adj[i])
            tmp = val
            for num in top_k[:min(k, len(top_k))]:
                tmp += vals[num]
            res = max(res, tmp)

        return res


