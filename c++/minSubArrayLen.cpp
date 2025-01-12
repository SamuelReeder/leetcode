class Solution {
public:
    int minSubArrayLen(int target, vector<int>& nums) {
        
        int current = 0;
        int best = INT_MAX;
        int s = 0, e = 0;  

        while (e < nums.size()) {

            current += nums[e];

            while (current >= target) {
                best = min(best, e - s + 1);
                current -= nums[s];
                s++;
            }

            e++;
        }

        if (best == INT_MAX) return 0;

        return best;
    }
};
