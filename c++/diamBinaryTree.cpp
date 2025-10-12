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

using T = std::tuple<int, int>;

class Solution {
public:

    T diameter(TreeNode* root) {
        // start at root
        if (root == nullptr) {
            return T{-1, -1};
        }

        if (root->left == nullptr && root->right == nullptr) {
            return T{0, 0};
        }

        auto l = diameter(root->left);
        auto r = diameter(root->right);

        int d = std::get<1>(l) + std::get<1>(r) + 2;
        int h = 1 + max(std::get<1>(l), std::get<1>(r));

        auto m = d;
        for (auto &i : {std::get<0>(l), std::get<0>(r)}) {
            if (m < i) {
                m = i;
            }
        }

        return T{m, h};
    }

    int diameterOfBinaryTree(TreeNode* root) {
        auto d = diameter(root);
        return max(std::get<0>(d), std::get<1>(d));
    }
};
