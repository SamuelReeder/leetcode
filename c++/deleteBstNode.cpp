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
    TreeNode* getSuccessor(TreeNode* curr){
        curr = curr->right;
        while (curr != nullptr && curr->left != nullptr)
            curr = curr->left;
        return curr;
    }

    TreeNode* deleteNode(TreeNode* root, int key) {
        
        if (!root)
            return root;

        if (key < root->val) {
            root->left = deleteNode(root->left, key);
        } else if (key > root->val) {
            root->right = deleteNode(root->right, key);
        } else {
            if (root->left == nullptr) {
                auto temp = root->right;
                delete root;
                return temp;
            }

            if (root->right == nullptr) {
                auto temp = root->left;
                delete root;
                return temp;
            }
            auto succ = getSuccessor(root);
            root->val = succ->val;
            root->right = deleteNode(root->right, succ->val);

        }a

        return root;
    }
};
