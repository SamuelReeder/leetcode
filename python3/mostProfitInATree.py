from math import inf
from collections import defaultdict

class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        n = len(edges) + 1
        
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        parent = [-1] * n
        visited = [False] * n
        queue = [0]
        visited[0] = True
        
        for node in queue:
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    parent[neighbor] = node
                    queue.append(neighbor)
        
        bob_path = []
        curr = bob
        while curr != -1:
            bob_path.append(curr)
            curr = parent[curr]
        
        bob_times = {node: i for i, node in enumerate(bob_path)}
        
        def dfs(node, par, step):
            cost = amount[node]
            if node in bob_times:
                if bob_times[node] == step:
                    cost //= 2
                elif bob_times[node] < step:
                    cost = 0
            
            children = [neighbor for neighbor in graph[node] if neighbor != par]
            
            if not children:
                return cost
            
            return cost + max(dfs(child, node, step + 1) for child in children)
        
        return dfs(0, -1, 0)
