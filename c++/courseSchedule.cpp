class Solution {
public:

    bool topologicalSortUtil(int i, vector<vector<int>>& adj, vector<bool>& visited, vector<bool>& recStack) {

        visited[i] = true;
        recStack[i] = true;

        for (int j : adj[i]) {
            if (!visited[j]) {
                if (!topologicalSortUtil(j, adj, visited, recStack)) {
                    return false;
                }
            }
            else if (recStack[j]){ 
                return false;
            }
        }
        
        recStack[i] = false;
        return true;
    }


    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        
        vector<vector<int>> adj(numCourses);

        for (vector<int> course : prerequisites) {
            adj[course[0]].push_back(course[1]);
        }

        vector<bool> visited(numCourses, false);
        vector<bool> recStack(numCourses, false);

        for (int i = 0; i < numCourses; i++) {
            if (!visited[i]) {
                if (!topologicalSortUtil(i, adj, visited, recStack)) {
                    return false; // Cycle detected
                }
            }
        }

        return true;
    }
};
