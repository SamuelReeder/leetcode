# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return
            
        dummy = ListNode(0, head)

        ls = []
        tmp = head
        while tmp:
            ls.append(tmp)
            tmp = tmp.next

        k = k % len(ls)

        # l - k is start of list
        tmp = dummy.next
        dummy.next = ls[-k]
        ls[-1].next = tmp
        ls[-k - 1].next = None
        
        return dummy.next

