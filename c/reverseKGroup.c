/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* reverseKGroup(struct ListNode* head, int k) {
    if (k <= 1 || head == NULL) {
        return head;
    }
    
    struct ListNode* curr = head;
    int count = 0;
    for (count = 0; count < k; count++) {
        if (curr == NULL) {
            return head; 
        }
        curr = curr->next;
    }
    
    curr = head;
    struct ListNode* prev = NULL;
    struct ListNode* next = NULL;
    
    for (count = 0; count < k; count++) {
        next = curr->next;
        curr->next = prev;
        prev = curr;
        curr = next;
    }
    
    head->next = reverseKGroup(curr, k);
    
    return prev;
    
}
