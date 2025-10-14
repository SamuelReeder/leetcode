class Solution {
public:
    string repeatLimitedString(string s, int repeatLimit) {
        // thinking we populate a hash map
        // we need some way to sort the map
        // maybe a max heap
        // for each element of map
        // insert into max heap
        // subtract 3 from count
        // when a letter added
        // access repeat and add back into heap
        // after next element


        unordered_map<char,int> repeat;
        for (char c : s) {
            if (repeat.find(c) == repeat.end()) {
                repeat[c] = 1;
            } else {
                repeat[c]++;
            }
        }

        priority_queue<pair<int,int>> pq;
        for (const auto& pair : repeat) {
            pq.push({pair.first, pair.second});
        }

        string res = "";
        while (!pq.empty()) {
            auto [c, count] = pq.top(); pq.pop();
            res.append(min(count, repeatLimit), c);

            int diff = count - repeatLimit;

            if (!pq.empty() && diff > 0) {

                auto [c2, count2] = pq.top(); pq.pop();
                res.append(1, c2);

                int diff2 = count2 - 1;
                if (diff2 > 0) {
                    pq.push({c2, diff2});
                }

                pq.push({c, diff});
            }
        }

        return res;
    }
};
