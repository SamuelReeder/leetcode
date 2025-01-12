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

    void dfs_recursive(TreeNode* root, vector<int> &side, int depth){
    
        if (root == NULL) return;

        if (side.size() < depth) {
            side.push_back(root->val);
        }

        dfs_recursive(root->right, side, depth + 1); 
        dfs_recursive(root->left, side, depth + 1); 
    }

    vector<int> rightSideView(TreeNode* root) {
        
        std::vector<int> side;
        dfs_recursive(root, side, 1);         

        return side;
    }
};
