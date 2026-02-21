class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # bfs or dfs with early return
        m, n = len(board), len(board[0])
        def helper(i, j, cnt):
            if cnt == len(word):
                return True

            tmp = board[i][j]
            board[i][j] = None

            adj = [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]
            for k, l in adj:
                if 0 > k or k >= m or 0 > l or l >= n or not board[k][l]:
                    continue
                
                if board[k][l] == word[cnt] and helper(k, l, cnt + 1):
                    return True

            board[i][j] = tmp 

            return False

        return any(helper(i, j, 1) for i in range(m) for j in range(n) if board[i][j] == word[0])
            


