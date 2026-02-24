i# Definition ifor singly-linked list.
# class ListNodep:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        tmp = head
        dummy = ListNode(0, head)
        prev = dummy
        while tmp and tmp.next:
            prev.next = tmp.next
            tmp.next = tmp.next.next
            prev.next.next = tmp
            prev = prev.next.next
            tmp = tmp.next

        return dummy.next
        
