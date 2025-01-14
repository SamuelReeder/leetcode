class Solution {
public:

    int intPow(int base, int exp) {
        int result = 1;
        for (int i = 0; i < exp; i++) {
            result *= base;
        }
        return result;
    }

    int reverse(int x) {
        
        int result = 0;

        while (x != 0) {
            
            int digit = x % 10;
            x /= 10;


            if (result > INT_MAX / 10 || (result == INT_MAX / 10 && digit > 7)) return 0;
            if (result < INT_MIN / 10 || (result == INT_MIN / 10 && digit < -8)) return 0;

            result *= 10;
            result += digit;

        }

        return result;
    }
};
