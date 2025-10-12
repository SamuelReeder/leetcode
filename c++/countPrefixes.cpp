class Solution {
public:
    int countPrefixes(vector<string>& words, string s) {

        return std::count_if(words.begin(), words.end(), [&](auto word){
            return s.starts_with(word);
        });

    }
};
