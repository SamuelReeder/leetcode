// not a great solution

using T = std::tuple<int,int,int>;

struct CmpFirst {
    bool operator()(const T& a, const T& b) const {
        return std::get<0>(a) > std::get<0>(b);
    }
};

class DSU {
    vector<int> parent, rank;

public:
    DSU(int n) {
        parent.resize(n);
        rank.resize(n);
        for (int i = 0; i < n; i++) {
            parent[i] = i;
            rank[i] = 1;
        }
    }

    int find(int i) {
        return (parent[i] == i) ? i : (parent[i] = find(parent[i]));
    }

    void unite(int x, int y) {
        int s1 = find(x), s2 = find(y);
        if (s1 != s2) {
            if (rank[s1] < rank[s2]) parent[s1] = s2;
            else if (rank[s1] > rank[s2]) parent[s2] = s1;
            else parent[s2] = s1, rank[s1]++;
        }
    }
};

using MinPQ = std::priority_queue<T, std::vector<T>, CmpFirst>;

class Solution {
public:

    int kruskalsMST(int V, MinPQ &edges) {
        
        DSU dsu(V);
        int cost = 0, count = 0;
        
        while (!edges.empty()) {

            auto e = edges.top();
            edges.pop();

            int w = get<0>(e), x = get<1>(e), y = get<2>(e);
            
            // Make sure that there is no cycle
            if (dsu.find(x) != dsu.find(y)) {
                dsu.unite(x, y);
                cost += w;
                if (++count == V - 1) break;
            }
        }
        return cost;
    }

    int minCostConnectPoints(vector<vector<int>>& points) {
        // total minimum cost
        
        MinPQ min_pq;

        for (int i = 0; i < points.size(); i++) {

            for (int j = i + 1; j < points.size(); j++) {
                auto p = points[i], q = points[j];

                int val = abs(p[0] - q[0]) + abs(p[1] - q[1]);

                min_pq.push(T{val, i, j});
            }
        }

        return kruskalsMST(points.size(), min_pq);
    }
};
