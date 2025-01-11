class Solution {
public:
    bool repeated(vector<char> nums, char target) {
        for (char num : nums) {
            if (num == target) {
                return true;
            }
        }
        return false;
    }

    bool isValidSudoku(vector<vector<char>>& board) {
        for (int i = 0; i < 9; i++) {
            vector<char> row = board[i];
            vector<char> nums;
            for (int j = 0; j < 9; j++) {
                if (row[j] == '.') {
                    continue;
                }

                if (repeated(nums, row[j])) {
                    return false;
                }
                nums.push_back(row[j]);
            }
        }

        for (int i = 0; i < 9; i++) {
            vector<char> nums;
            for (int j = 0; j < 9; j++) {
                if (board[j][i] == '.') {
                    continue;
                }
                
                if (repeated(nums, board[j][i])) {
                    return false;
                }
                nums.push_back(board[j][i] );
            }
        }

        for (int i = 0; i < 9; i += 3) {            
            for (int j = 0; j < 9; j += 3) {

                vector<char> nums;
                for (int k = i; k < i + 3; k++) {
                    for (int h = j; h < j + 3; h++) {
                        if (board[k][h] == '.') {
                            continue;
                        }
                        
                        if (repeated(nums, board[k][h])) {
                            return false;
                        }

                        nums.push_back(board[k][h]);
                    }
                }
            }
        }

        return true;
    }
}
