o
Samuel Reeder <samuel.reeder8@gmail.com>
Tue, Oct 28, 3:58 PM (1 day ago)
to me

class Solution {
public:
    int largestRectangleArea(vector<int>& heights) {
        const int n = heights.size();

        // loop through each i and find the first one less than heights[i] to left and right

        // use a monotonous increasing stack
        // push element makes pop all higher elements until its the greatest element
        
        // if you push in heights[i], all elements >= to it will be popped
        // the element before is therefore the element less than it, so thats when the rectangle ends

        // we put indices into the stack, but compare based on heights[stack.top()]

        stack<int> mit;
        stack<int> rev_mit;

        vector<int> dp(n, 0);

        for (int i = 0; i < n; i++) {
            
            const int h = heights[i];

            while (!mit.empty() && heights[mit.top()] >= h) {
                mit.pop();
            }

            const int cnt = mit.empty() ? i + 1 : i - mit.top();
            dp[i] = cnt * h;

            mit.push(i);
        }

        int m = 0;
        for (int i = n - 1; i >= 0; i--) {
            
            const int h = heights[i];

            while (!rev_mit.empty() && heights[rev_mit.top()] >= h) {
                rev_mit.pop();
            }

            const int cnt = rev_mit.empty() ? n - i : rev_mit.top() - i;
            dp[i] += (cnt - 1) * h;
            m = max(m, dp[i]);

            rev_mit.push(i);
        }
        return m;
    }
};
