class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        
        int len = 0;
        int longest = 0;

        unordered_map<char, int> freq;
        for (int i = 0; i < s.length(); i++) {

            
            // for (auto itr = freq.begin(); 
            //     itr != freq.end(); itr++) 
            // {
            //     // itr works as a pointer to 
            //     // pair<string, double> type 
            //     // itr->first stores the key part and
            //     // itr->second stores the value part
            //     cout << itr->first << "  " << 
            //             itr->second << endl;
            // }

            if (freq.find(s[i]) == freq.end() || freq[s[i]] < i - len) {
                freq[s[i]] = i;
                len++;
            } else {
                longest = max(longest, len);
                
                len =  i - freq[s[i]];
                freq[s[i]] = i;
            }

        }
        return max(longest, len);
    }
};
