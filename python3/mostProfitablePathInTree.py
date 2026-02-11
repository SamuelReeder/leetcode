class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        
        # fix bob
        # dfs for alice

        adj_list = [[] for _ in range(len(edges) + 1)] 
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)

        # we need to deduct bobs contribution from alices for eacha applicable node
        # basically if at alices turn i, bob has been at node for some turn < i
        # the node is free
        # if at turn i bob is also at i
        # node is half the cost
        # make a map of node: turn

        bob_history = {bob: 0}
        def dfsBob(node, prev, time):

            if node == 0:
                return 0

            chosen = None
            minimum = float('inf')
            for i in adj_list[node]:
                if i == prev:
                    continue
                
                tmp = dfsBob(i, node, time + 1)
                if tmp < minimum:
                    chosen = i
                    minimum = tmp 
            
            bob_history[chosen] = time + 1

            return 1 + minimum

        _ = dfsBob(bob, -1, 0)

        def dfs(node, depth, prev):
            cost = amount[node]
            if node in bob_history:
                if bob_history[node] < depth:
                    cost = 0
                elif bob_history[node] == depth:
                    cost //= 2

            maximum = float('-inf')
            for i in adj_list[node]:
                if i == prev:
                    continue
                maximum = max(dfs(i, depth + 1, node), maximum)

            return cost + maximum if maximum != float('-inf') else cost

        return dfs(0, 0, -1)

