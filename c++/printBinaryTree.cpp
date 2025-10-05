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
private:
    int height(TreeNode* root) {
        if (root == nullptr) {
            return -1;
        }
        return 1 + max(height(root->left), height(root->right));
    }

    void fill(vector<vector<string>>& res, TreeNode* node, int r, int c, int h) {
        if (node == nullptr) {
            return;
        }
        res[r][c] = to_string(node->val);
        
        if (h - r - 1 < 0)
            return; 
            
        int colOffset = 1 << (h - r - 1); // 2^(h - r - 1)
        fill(res, node->left, r + 1, c - colOffset, h);
        fill(res, node->right, r + 1, c + colOffset, h);
    }

public:
    vector<vector<string>> printTree(TreeNode* root) {
        int h = height(root);
        int m = h + 1;
        int n = (1 << (h + 1)) - 1; // 2^(h + 1) - 1
        
        vector<vector<string>> res(m, vector<string>(n, ""));
        
        int root_col = (n - 1) / 2;
        fill(res, root, 0, root_col, h);
        
        return res;
    }
};
