class Solution {
public:
    int singleNumber(vector<int>& nums) {
        // loop through each and apply bitmask
        // for each that appears twice
        int mask = 0;
        for (auto i : nums) {
            mask ^= i;
        }
        
        return mask;
    }
};
