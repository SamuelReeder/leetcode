class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {

        unordered_map<int, vector<int>> indexMap;
        for (int i = 0; i < nums.size(); i++) {
            indexMap[nums[i]].push_back(i);
        }

        vector<int> nums2(nums);
        sort(nums2.begin(), nums2.end());

        int i = 0, j = nums2.size() - 1;
        while (i < j) {
            int temp = nums2[i] + nums2[j];
            if (temp < target) {
                i++;
            } else if (temp > target) {
                j--;
            } else {
                break;
            }
        }

        vector<int> result;
        result.push_back(indexMap[nums2[i]].back());
        indexMap[nums2[i]].pop_back();
        result.push_back(indexMap[nums2[j]].back());
        indexMap[nums2[j]].pop_back();

        return result;
    }
};
