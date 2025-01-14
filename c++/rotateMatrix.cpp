class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        
        // M[i, j] = M[j, i]

        // M[i, j] = M[j, N - i - 1]

        int m = matrix.size(), n = matrix[0].size();
        for (int i = 0; i < m; i++) {
            for (int j = i; j < n; j++) {
                int temp = matrix[i][j];
                matrix[i][j] = matrix[j][i];
                matrix[j][i] = temp;
            }
        } 

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n/2; j++) {
                int temp = matrix[i][j];
                matrix[i][j] = matrix[i][n - j - 1];
                matrix[i][n - j - 1] = temp;
            }
        } 

    }
};
