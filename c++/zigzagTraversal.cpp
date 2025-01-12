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
// class Solution {
// public:
//     vector<vector<int>> zigzagLevelOrder(TreeNode* root) {

//         // first add root
//         // then add left then right
//         // then pop from front and add each to back
        
//         vector<vector<int>> zigzag;

//         if (!root) return zigzag;

//         deque<TreeNode*> dq; 

//         dq.push_back(root);

//         bool going_right = true;

//         while (!dq.empty()) {

//             int size = dq.size();
//             vector<int> group;

//             for (int i = 0; i < size; i++) {

//                 if (going_right) {
//                     TreeNode* temp = dq.front();
//                     dq.pop_front();

//                     group.push_back(temp->val);

//                     if (temp->left) dq.push_back(temp->left);
//                     if (temp->right) dq.push_back(temp->right);
//                 } else {
//                     TreeNode* temp = dq.back();
//                     dq.pop_back();

//                     group.push_back(temp->val);

//                     if (temp->right) dq.push_front(temp->right);
//                     if (temp->left) dq.push_front(temp->left);
//                 }
//             }

//             going_right = !going_right;

//             zigzag.push_back(group);
//         }

//         return zigzag;
//     }
// };

class Solution {
public:
    vector<vector<int>> zigzagLevelOrder(TreeNode* root) {

        vector<vector<int>> zigzag;

        if (!root) return zigzag;

        queue<TreeNode*> q; 

        q.push(root);

        bool going_right = true;

        while (!q.empty()) {

            int size = q.size();
            vector<int> group;

            for (int i = 0; i < size; i++) {

                TreeNode* temp = q.front();
                q.pop();

                group.push_back(temp->val);

                if (temp->left) q.push(temp->left);
                if (temp->right) q.push(temp->right);
            }

            if (!going_right) {
                reverse(group.begin(), group.end());
            }

            going_right = !going_right;

            zigzag.push_back(group);
        }

        return zigzag;
    }
};
