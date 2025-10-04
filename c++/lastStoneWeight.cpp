class Solution {
public:
    int lastStoneWeight(vector<int>& stones) {
        std::priority_queue<int> q(stones.begin(), stones.end());

        while (q.size() > 1) {

            int y = q.top();
            q.pop();

            if (y != q.top()) {
                int x = q.top();
                q.pop();
                // y - x = z
                q.push(y - x);
            } else {
                q.pop();
            }
        }

        return q.empty() ? 0 : q.top();
    }
};
