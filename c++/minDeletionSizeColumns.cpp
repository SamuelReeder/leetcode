class Solution {
public:
    int minDeletionSize(vector<string>& strs) {
        int count = 0;
        const int m = strs[0].size();
        const int n = strs.size();
        for (int i = 0; i < m; i++) {
            int last = strs[0][i];
            for (int j = 1; j < n; j++) {
                int num = int(static_cast<unsigned char>(strs[j][i]));
                if (num < last) {
                    count++;
                    break;
                }
                last = num;
            }
        }

        return count;
    }
};
