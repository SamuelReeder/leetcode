class Solution {
public:
    bool canBeValid(string s, string locked) {
        
        if (s.length() % 2) return false;
        
        int balance = 0, wild = 0;
        for (int i = 0; i < s.length(); i++) {
            if (locked[i] == '0') {
                wild++;
            } else if (s[i] == '(') {
                balance++;
            } else {
                balance--;
            }
            
            if (wild + balance < 0) return false;
        }
        
        balance = 0;
        wild = 0;
        for (int i = s.length() - 1; i >= 0; i--) {
            if (locked[i] == '0') {
                wild++;
            } else if (s[i] == ')') {
                balance++;
            } else {
                balance--;
            }
            
            if (wild + balance < 0) return false;
        }
        
        return true;
    }
};
