class Solution {
public:
    void setZeroes(vector<vector<int>>& matrix) {
        
        int firstRow = -1, firstCol = -1;
        int m = matrix.size(), n = matrix[0].size();
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (matrix[i][j] == 0) {
                    if (firstRow == -1) {
                        firstRow = i;
                        firstCol = j;
                    } else {
                        matrix[firstRow][j] = 0;
                        matrix[i][firstCol] = 0;
                    }
                }
            }
        }

        if (firstRow == -1) return;

        for (int i = 0; i < m; i++) {
            if (i != firstRow && matrix[i][firstCol] == 0) {
                for (int j = 0; j < n; j++) {
                    matrix[i][j] = 0;
                }
            }
        }

        for (int j = 0; j < n; j++) {
            if (j != firstCol && matrix[firstRow][j] == 0) {
                for (int i = 0; i < m; i++) {
                    matrix[i][j] = 0;
                }
            }
        }

        for (int j = 0; j < n; j++) {
            matrix[firstRow][j] = 0;
        }

        for (int i = 0; i < m; i++) {
            matrix[i][firstCol] = 0;
        }
    }
};
