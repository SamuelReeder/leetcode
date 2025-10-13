#include <limits.h>

class Solution {
public:
    int nthSuperUglyNumber(int n, vector<int>& primes) {
        
        vector<long long> dp(n, INT_MAX);
        dp[0] = 1;

        // sun is always sorted, so is primes
        // so lowest will be front of sun * front of prime
        vector<int> pointers(primes.size(), 0);
        for (int i = 1; i < n; i++) {

            vector<int> idx;
            for (int j = 0; j < primes.size(); j++) {

                // if (dp[pointers[j]] == INT_MAX)
                //     continue;

                long long sun = primes[j] * dp[pointers[j]];
                
                if (dp[i] > sun) {
                    dp[i] = sun;
                    idx.clear();
                    idx.push_back(j);
                } else if (dp[i] == sun) {
                    idx.push_back(j);
                }
            }

            for (auto k : idx) {
                pointers[k]++;
            }
        }

        // for (auto i : dp ) {
        //     std::cout << "number " << i << std::endl;
        // }

        return static_cast<int>(dp[n - 1]);
    }
};
