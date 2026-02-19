# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        tmp, last = head, None
        while tmp is not None:
            if last and tmp.val == last.val:
                last.next = tmp.next
            else:
                last = tmp

            tmp = tmp.next

        return head
