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
    void rec(TreeNode* root, vector<int>& leafs) {
        if (!root->right && !root->left) {
            leafs.push_back(root->val);
            return;
        }

        if (root->left) rec(root->left, leafs);
        if (root->right) rec(root->right, leafs);
    }

    bool leafSimilar(TreeNode* root1, TreeNode* root2) {
        
        vector<int> root1Leafs, root2Leafs;
        
        rec(root1, root1Leafs);
        rec(root2, root2Leafs);

        if (root1Leafs.size() != root2Leafs.size()) return false;

        for (int i = 0; i < root1Leafs.size(); i++) {
            if (root1Leafs[i] != root2Leafs[i]) return false;
        }

        return true;
    }
};
