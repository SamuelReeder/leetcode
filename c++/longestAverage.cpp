class Solution {
public:
    double findMaxAverage(vector<int>& nums, int k) {
        
        double current = 0, m = INT_MIN;
        for (int i = 0; i < nums.size(); i++) {
            if (i >= k - 1) {
                current += nums[i];
                m = max(m, current / k);
                current -= nums[i - k + 1];
            } else {
                current += nums[i];
            }
        }

        return m;
    }
};
