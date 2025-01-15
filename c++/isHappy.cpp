class Solution {
public:
    bool isHappy(int n) {
        unordered_set<int> numSet;

        while (n != 1 && numSet.find(n) == numSet.end()) {
            numSet.insert(n);
            int sum = 0;
            while (n != 0) {
                sum += pow(n % 10, 2);
                n /= 10;
            }
            n = sum;
        }

        return n == 1;
    }
};
