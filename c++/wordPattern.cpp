class Solution {
public:
    bool wordPattern(string pattern, string s) {
        std::unordered_map<char, string> bijection;
        std::unordered_map<string, char> reverse;

        std::istringstream iss(s);

        int i = 0;
        do {
            string subs;
    
            iss >> subs;

            if (bijection.find(pattern[i]) != bijection.end() && bijection[pattern[i]] != subs) {
                return false;
            }

            if (reverse.find(subs) != reverse.end() && reverse[subs] != pattern[i]) {
                return false;
            }

            bijection[pattern[i]] = subs;
            reverse[subs] = pattern[i];
            i++;
    
        } while (iss);

        if (i != pattern.length() + 1){
            return false;
        }

        return true;
    }
};
