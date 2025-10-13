class Solution {
public:
    bool isUgly(int n) {
        
        if (n == 1)
            return true;

        vector<int> factors = {2, 3, 5};

        while (n > 1) {
            int tmp = n;
            for (auto factor : factors) {
                if (n % factor == 0) {
                    n /= factor;
                }
            }

            if (tmp == n)
                return false;
        }

        return n == 1;
    }
};
