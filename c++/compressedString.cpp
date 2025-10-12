class Solution {
public:
    string compressedString(string word) {
        
        string comp = "";
        int n = word.size();

        char letter = 0;
        size_t count = 0;
        for (int i = 0; i < n; i++) {

            // need to check number of times first letter appear

            if (!letter) {
                letter = word[i];                
            } else if (letter != word[i] || count == 9) {
                comp.push_back(count+'0');
                comp.push_back(letter);
                count = 0;
                letter = word[i];
            }

            count++;
        }

        if (letter) {
            comp.push_back(count+'0');
            comp.push_back(letter);
        }

        return comp;
    }
};
