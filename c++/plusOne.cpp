class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {

        for (auto it = digits.rbegin(); it != digits.rend(); ++it) {

            if (*it + 1 == 10) {
                *it = 0;
                continue;
            }

            *it += 1;
            return digits;
        }   

        digits.insert(digits.begin(), 1);

        return digits;
    }
};
