class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        
        int s = 0, e = nums.size();
        while (s < e) {
            int m = s + (e - s) / 2;

            if (nums[m] < target) {
                s = m + 1;
            } else if (nums[m] > target) {
                e = m;
            } else {
                return m;
            }
        }

        return s;
    }
};
