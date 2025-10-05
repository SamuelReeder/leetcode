class Solution {
public:
    int maxIncreaseKeepingSkyline(vector<vector<int>>& grid) {
        // for each direction:
        // can save the maximum height of each row/column of the skyline
        // for east/west, we save the maximum column of each row in maxCol
        // for north/south, we save the maximum row of each column in maxRow

        // for each index [i][j], we check if grid[i][j] >= any of maxRow[i] or maxCol[j]
        // if it is, we can't increase
        // if it isn't we can increase up to the difference of the max
         
        const int n = grid[0].size();
        std::vector<int> maxRow(n, 0);
        std::vector<int> maxCol(n, 0);

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                maxRow[i] = std::max(maxRow[i], grid[i][j]);
                maxCol[j] = std::max(maxCol[j], grid[i][j]);
            }
        }

        int amount = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                
                int diffHoriz = maxRow[i] - grid[i][j];
                int diffVert = maxCol[j] - grid[i][j];

                amount += std::min(diffVert, diffHoriz);
            }
        }

        return amount;
    }
};
