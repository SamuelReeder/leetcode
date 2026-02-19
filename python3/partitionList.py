# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        
        g = last_g = ListNode()
        l = last_l = ListNode()

        tmp = head
        while tmp is not None:
            if tmp.val < x:
                last_l.next = tmp
                last_l = last_l.next
            else:
                last_g.next = tmp
                last_g = last_g.next

            tmp = tmp.next

        last_l.next = g.next
        last_g.next = None

        return l.next
