/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    vector<int> ll;
    Solution(ListNode* head) {
        auto tmp = head;
        while (tmp != NULL) {
            ll.push_back(tmp->val);
            tmp = tmp->next;
        }
    }
    
    int getRandom() {
        return ll[static_cast<int>(rand() % ll.size())];
    }
};

/**
 * Your Solution object will be instantiated and called as such:
 * Solution* obj = new Solution(head);
 * int param_1 = obj->getRandom();
 */
