class Solution {
public:
    vector<string> letterCombinations(string digits) {
        
        unordered_map<char, string> phone = {
            {'2', "abc"}, {'3', "def"}, {'4', "ghi"},
            {'5', "jkl"}, {'6', "mno"}, {'7', "pqrs"},
            {'8', "tuv"}, {'9', "wxyz"}
        };

        vector<string> combinations;

        for (char digit : digits) {
            vector<string> temp;
            const string& letters = phone[digit];

            if (combinations.empty()) {
                for (char letter : letters) {
                    temp.push_back(string(1, letter));
                }
            } else {
                for (const string& combination : combinations) {
                    for (char letter : letters) {
                        temp.push_back(combination + letter);
                    }
                }
            }

            combinations.swap(temp);
        }

        return combinations;
    }
};
