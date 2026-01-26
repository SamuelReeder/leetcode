class Solution {
public:
    bool isCircularSentence(string sentence) {
        
        std::stringstream ss(sentence);
        std::string token, last;
        while (ss >> token) {
            if (!last.empty() && last.back() != token[0]) {
                return false;
            }
            last = token;
        }

        return last.back() == sentence[0];
    }
};
