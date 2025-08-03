#include <cmath>

class Solution {
public:
    bool isPrime(int num) {
        
        if (num == 1)
            return false;

        for (int i = sqrt(num); i > 1; i--) {
            if (num % i == 0) {
                return false;
            }
        }
        return true;
    }

    int maximumPrimeDifference(vector<int>& nums) {
        int i = nums.size() - 1;
        int j = 0;

        while (j < i) {
            bool more = false;
            if (!isPrime(nums[i])) {
                more = true;
                i--;
            }

            if (!isPrime(nums[j])) {
                more = true;
                j++;
            }

            if (!more)
                return i - j;
        }

        return 0;
    }
};
