class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        
        # this is a graph problem
        # paths is a list of edges
        # there are n nodes

        if n == 1:
            return [1]

        answer = [0] * n
        edges = {i: set() for i in range(1, n + 1)}

        colors = {1,2,3,4}

        for x, y in paths:
            edges[x].add(y)
            edges[y].add(x)

        for i in range(1, n + 1):
            answer[i - 1] = list(colors - {answer[i - 1] for i in edges[i]})[0]
            
        return answer


