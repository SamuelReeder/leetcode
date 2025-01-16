/** 
 * Forward declaration of guess API.
 * @param  num   your guess
 * @return 	     -1 if num is higher than the picked number
 *			      1 if num is lower than the picked number
 *               otherwise return 0
 * int guess(int num);
 */

class Solution {
public:
    int guessNumber(int n) {

        int g, m;
        int low = 1, high = n;
        while (true) {
            m = (high - low) / 2 + low;
            g = guess(m);

            if (g == -1) {
                high = m - 1;
            } else if (g == 1) {
                low = m + 1;
            } else {
                break;
            }
        }

        return m;
        
    }
};
