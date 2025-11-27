class Solution {
public:
    int countAsterisks(string s) {
        
        int total = 0;
        int cnt = 0;
        int bar_cnt = 0;
        for (char c : s) {
            
            if (c == '|') {
                if (++bar_cnt % 2 != 0) {
                    total += cnt;
                }
                cnt = 0;
            } else if (c == '*') {
                cnt++;
            }

        }

        return total + cnt;

    }
};
