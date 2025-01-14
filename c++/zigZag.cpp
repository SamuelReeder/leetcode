class Solution {
public:
    string convert(string s, int numRows) {
        
        if (numRows == 1 || s.length() <= numRows) {
            return s;
        }
        
        string zigzag;
        zigzag.reserve(s.length());
        
        int cycle = 2 * (numRows - 1);
        
        for (int i = 0; i < numRows; i++) {
            for (int j = i; j < s.length(); j += cycle) {
                zigzag += s[j];
                
                if (i > 0 && i < numRows - 1) {
                    int intermediate = j + cycle - 2 * i;
                    if (intermediate < s.length()) {
                        zigzag += s[intermediate];
                    }
                }
            }
        }
        
        return zigzag;
    }
};
