class Solution {
public:
    string reversePrefix(string word, char ch) {
        
        int idx = 0;
        for (int i = 0; i < word.length(); i++) {
            if (word[i] == ch) {
                idx = i; 
                break;
            }
        }

        for (int i = 0; i < (idx + 1) / 2; i++) {
            auto tmp = word[i];
            word[i] = word[idx - i];
            word[idx - i] = tmp;
        }

        return word;
    }
};
