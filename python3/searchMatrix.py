class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        
        # flattened 1d array
        left = 0
        right = m * n - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            row = mid // n
            col = mid % n
            mid_val = matrix[row][col]
            
            if mid_val == target:
                return True
            elif mid_val < target:
                left = mid + 1
            else:
                right = mid - 1
                
        return False
