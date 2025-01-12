/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    vector<double> averageOfLevels(TreeNode* root) {
        vector<double> averages;

        queue<TreeNode*> q;
        q.push(root);

        while (!q.empty()) {
            
            double size = q.size();
            double current = 0;

            for (int i = 0; i < size; i++) {
                TreeNode* temp = q.front();
                q.pop();
                current += temp->val;

                if (temp->left != NULL) {
                    q.push(temp->left);
                }

                if (temp->right != NULL) {
                    q.push(temp->right);
                }
            }

            averages.push_back(current / size);

        }

        return averages;
    }
};
