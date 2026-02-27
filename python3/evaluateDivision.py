class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # directed graph where answer of query is directed edges from dividend to divisor
        # a/b = 2
        # b/c = 3
        # a = 2b
        # b = 3c
        # a/2 = 3c
        # a/c = 6
        # reverse edge is 1/edge
        
        # construct the adjacency

        edges = defaultdict(dict)
        for i in range(len(values)):
            a, b = equations[i]
            edges[a][b] = values[i]
            edges[b][a] = 1/values[i]

        print(edges)
        def helper(q):
            a, b = q
            if a in self.seen:
                return -1
            
            self.seen.add(a)

            if b in edges[a]:
                return edges[a][b]

            for edge, weight in edges[a].items():
                tmp = helper((edge, b))
                if tmp != -1:
                    return weight * tmp

            return -1

        res = []
        for a, b in queries:
            self.seen = set()
            res.append(helper((a,b)))

        return res


