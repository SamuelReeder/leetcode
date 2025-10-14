class Solution {
public:
    long long gcd(int a, int b) {
        if (a == 0)
            return b;
        return gcd(b % a, a);
    }

    long long countPairs(vector<int>& nums, int k) {
        // every key is a divisor of k
        unordered_map<long long, int> hm;

        long long cnt = 0;

        for (int i = 0; i < nums.size(); i++) {

            long long g = gcd(k, nums[i]);
            if (g == 0) {
                continue;
            }
            

            // if (hm.contains(k / g)) {
            //     cnt += hm[k / g];
            // }

            for (auto [key, val] : hm) {
               if ((key * g) % k == 0) {
                    cnt += val;
               } 
            }

            if (!hm.contains(g)) {
                hm[g] = 1;
            } else {
                hm[g]++;
            }
        }

        return cnt;

    }
};
