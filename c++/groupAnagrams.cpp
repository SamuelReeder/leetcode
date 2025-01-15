class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        
        vector<vector<string>> result;
        unordered_map<string, int> hash;
        
        for (string& s : strs) {

            string t = s;
            sort(t.begin(), t.end());

            if (hash.find(t) == hash.end()) {
                hash[t] = result.size();
                vector<string> temp = {s};
                result.push_back(temp);
            } else {
                result[hash[t]].push_back(s);
            }
        }

        return result;
    }
};
