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

struct Compare {
    bool operator()(ListNode* a, ListNode* b) {
        return a->val > b->val;  // Min-heap: smallest element has the highest priority
    }
};

class Solution {
public:

    ListNode* mergeKLists(vector<ListNode*>& lists) {
        priority_queue<ListNode*, vector<ListNode*>, Compare> pq;

        for (auto list : lists) {
            if (list) pq.push(list);
        }

        ListNode* head = new ListNode(0);
        ListNode* current = head;
        
        while (!pq.empty()) {
            ListNode* temp = pq.top();
            pq.pop();

            current->next = temp;
            current = current->next;

            if (temp->next) pq.push(temp->next);
        }

        return head->next;
    }
};
