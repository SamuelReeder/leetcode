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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        
        std::vector<ListNode*> tmp = {head};
        // pointer to head
        auto curr = head;
        auto len = 1;
        while (curr->next != nullptr) {
            curr = curr->next;
            tmp.push_back(curr);
            len++;
        }

        auto num = len - n;

        if (num == 0) {
            return head->next;
        } else if (num == len - 1) {
            (tmp[num - 1])->next = nullptr;
            return head;
        }

        (tmp[num - 1])->next = tmp[num + 1];
        return head;

    }
};
