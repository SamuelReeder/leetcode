using W = tuple<int, int>;

class Solution {
public:
    vector<int> countPairsOfConnectableServers(vector<vector<int>>& edges, int signalSpeed) {
        
        int n = 0;
        for (auto& edge : edges) {
            n = max({edge[0], edge[1], n});
        }
        n++;

        vector<vector<W>> adj(n);
        for (auto& edge : edges) {
            int u = edge[0];
            int v = edge[1];
            int w = edge[2];
            adj[u].push_back({v, w});
            adj[v].push_back({u, w});
        }

        auto dfs = [&](auto&& self, int u, int p, int curr_dist) -> int {
            int count = 0;
            
            if (curr_dist % signalSpeed == 0) {
                count++;
            }

            for (auto& [v, w] : adj[u]) {
                if (v != p) {
                    count += self(self, v, u, curr_dist + w);
                }
            }
            return count;
        }; 

        vector<int> res(n);

        for (int i = 0; i < n; i++) {
            int total_pairs = 0;
            int prev_valid_nodes = 0;

            for (auto& [neighbor, weight] : adj[i]) {
                
                int count_in_branch = dfs(dfs, neighbor, i, weight);
                
                // Since root is fixed, all branches constitute paris
                total_pairs += count_in_branch * prev_valid_nodes;
                prev_valid_nodes += count_in_branch;
            }
            res[i] = total_pairs;
        }

        return res;
    }
};
