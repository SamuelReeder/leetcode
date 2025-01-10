class Solution {
public:

    string entry(int s, int num) {
        if (s == num) {
            return to_string(s);
        }
        return to_string(s) + "->" + to_string(num);
    }

    
    vector<string> summaryRanges(vector<int>& nums) {
        
        vector<string> result;
        
        if (nums.empty()) {
            return result;
        }

        int start = nums[0];
        int prev = nums[0];
        
        for (int i = 1; i <= nums.size(); i++) {
            if (i == nums.size() || nums[i] != prev + 1) {
                result.push_back(entry(start, prev));
                if (i < nums.size()) {
                    start = nums[i];
                }
            }
            if (i < nums.size()) {
                prev = nums[i];
            }
        }
        
        return result;
    }
};
