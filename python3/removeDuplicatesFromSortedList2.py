# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # O(1) space

        dummy = prev = ListNode(-101, head)
        tmp = head
        last = dummy.val
        while tmp:
            removed = False
            while tmp and tmp.next and tmp.val == tmp.next.val:
                removed = True
                tmp = tmp.next
            
            if not removed:
                prev = tmp
            else:
                prev.next = tmp.next

            tmp = tmp.next

        return dummy.next
