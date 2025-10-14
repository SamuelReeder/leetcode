class Solution {
public:
    bool isPowerOfTwo(int n) {
        // n will be 100000.... if power of 2
        // n - 1 is  011111....

        // 10000

        if (n <= 0)
            return false;

        long long num = (n & (n - 1));
        return num == 0;

    }
};
