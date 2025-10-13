#include <limits.h>

class Solution {
public:
    int nthSuperUglyNumber(int n, vector<int>& primes) {
        
        if (n == 1) return 1;

        int k = primes.size();
        vector<long long> dp(n, INT_MAX);
        dp[0] = 1;

        vector<int> pointers(k, 0);
        vector<long long> cand(k, INT_MAX);
        for (int i = 1; i < n; i++) {

            for (int j = 0; j < k; j++) {
                cand[j] = primes[j] * dp[pointers[j]];
                dp[i] = min(cand[j], dp[i]);
            }

            for (int j = 0; j < k; j++) {
                if (cand[j] <= dp[i])
                    pointers[j]++;
            }
        }

        // for (auto i : dp ) {
        //     std::cout << "number " << i << std::endl;
        // }

        return static_cast<int>(dp[n - 1]);
    }
};
