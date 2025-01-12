class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        vector<int> spiral;

        if (matrix.empty() || matrix[0].empty()) {
            return spiral;
        }

        int top = 0, bottom = matrix.size() - 1;
        int left = 0, right = matrix[0].size() - 1;

        while (top <= bottom && left <= right) {
            for (int i = left; i <= right; i++) {
                spiral.push_back(matrix[top][i]);
            }
            top++;

            for (int i = top; i <= bottom; i++) {
                spiral.push_back(matrix[i][right]);
            }
            right--;

            if (top <= bottom) {
                for (int i = right; i >= left; i--) {
                    spiral.push_back(matrix[bottom][i]);
                }
                bottom--;
            }

            if (left <= right) {
                for (int i = bottom; i >= top; i--) {
                    spiral.push_back(matrix[i][left]);
                }
                left++;
            }
        }

        return spiral;
    }
};
