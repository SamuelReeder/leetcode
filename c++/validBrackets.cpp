class Solution {
public:
    bool isValid(string s) {
        
        unordered_map<char, char> brackets = {{')', '('}, {'}', '{'}, {']', '['}};
        stack<char> vecStack;

        for (char& c : s) {
            if (brackets.find(c) == brackets.end()) {
                vecStack.push(c);
            } else if (!vecStack.empty()) {
                if (vecStack.top() != brackets[c]) {
                    return false;
                }
                vecStack.pop();
            } else {
                return false;
            }
        }

        return vecStack.empty();
    }
};
