class Solution {
public:
    bool isAnagram(string s, string t) {
        
        unordered_map<char, int> occurences;

        for (char& c : s) {
            
            if (occurences.find(c) == occurences.end()) {
                occurences[c] = 1;
            } else {
                occurences[c]++;
            }

        }

        int count = s.length();
        for (char& c : t) {
            if (occurences.find(c) == occurences.end() || occurences[c] == 0) {
                return false;
            } else {
                occurences[c]--;
                count--;
            }
        }

        return count == 0;
    }
};
