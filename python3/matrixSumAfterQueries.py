class Solution:
    def matrixSumQueries(self, n: int, queries: List[List[int]]) -> int:
        
        col = [0] * n
        row = [0] * n
        
        cols_cnt = 0
        rows_cnt = 0 

        total = 0
        for q in reversed(queries):
            t, i, v = q
            if t == 1 and col[i] == 0:
                col[i] = v
                cols_cnt += 1
                total += (n - rows_cnt) * v
            elif t == 0 and row[i] == 0:
                row[i] = v
                rows_cnt += 1
                total += (n - cols_cnt) * v

        return total

            

        

        

