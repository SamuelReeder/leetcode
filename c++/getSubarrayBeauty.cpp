class Solution {
public:
    vector<int> getSubarrayBeauty(vector<int>& nums, int k, int x) {
        
        const auto n = nums.size();

        vector<int> res(n - k + 1);
        vector<int> freq(51);
        for (int i = 0; i < n; i++) {

            if (nums[i] < 0) {
                freq[abs(nums[i])]++;
            }

            if (i < k - 1) continue;

            if (i >= k && nums[i - k] < 0) {
                freq[abs(nums[i - k])]--;
            }

            int cnt = 0;
            for (int j = 50; j > 0; j--) {
                cnt += freq[j];

                if (cnt >= x) {
                    res[i - k + 1] = j * -1;
                    break;
                }
            }
        }

        return res;

    }
};
