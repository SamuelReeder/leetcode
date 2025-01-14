class Solution {
public:
    bool isSubsequence(string s, string t) {
        
        int j = 0;
        for (char& c : s) {
            
            while (c != t[j] && j < t.length()) {
                j++;
            }

            if (c == t[j]) {
                j++;
                continue;
            }

            return false;
        }

        return true;
    }
};
