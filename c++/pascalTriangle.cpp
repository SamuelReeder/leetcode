class Solution {
public:
    vector<vector<int>> generate(int numRows) {
        using namespace std;
        
        vector<vector<int>> triangle(1, {1});

        for (int i = 0; i < numRows - 1; i++) {

            int rowSize = triangle[i].size() + 1;
            vector<int> row(rowSize);

            for (int j = 0; j < rowSize; j++) {

                if (j > 0)
                    row[j] += triangle[i][j - 1];

                if (j < triangle[i].size())
                    row[j] += triangle[i][j];
            }

            triangle.push_back(row);
        }

        return triangle;

    }
};
