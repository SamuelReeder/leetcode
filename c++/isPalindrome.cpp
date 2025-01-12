class Solution {
public:
    bool isPalindrome(string s) {
        
        // could also just keep pointers for front and back and do a half loop
        string parsed = "";
        for (char c : s) {
            if (isalnum(c)) {
                parsed += tolower(c);
            }
        }

        for (int i = 0; i < parsed.length(); i++) {
            if (parsed[i] != parsed[parsed.length() - 1 - i]) {
                return false;
            }
        }

        return true;
    }
};
