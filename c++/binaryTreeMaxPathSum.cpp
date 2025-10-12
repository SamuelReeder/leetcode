
#include <limits.h>

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
        if (!root) return {INT_MIN, 0};

        auto [bestL, downL] = diameter(root->left);
        auto [bestR, downR] = diameter(root->right);

        // clamp negatives
        int useL = std::max(0, downL);
        int useR = std::max(0, downR);

        int through = root->val + useL + useR;
        int down    = root->val + std::max(useL, useR);

        int best = std::max({bestL, bestR, through, down, root->val});
        return {best, down};
    }


    int maxPathSum(TreeNode* root) {
        auto d = diameter(root);
        return max(std::get<0>(d), std::get<1>(d));
    }
};
