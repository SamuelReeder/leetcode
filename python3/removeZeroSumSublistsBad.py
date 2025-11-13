# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        curr = head
        prev = []
        while curr is not None:
            
            prev.append(curr)

            s = 0
            for i in range(len(prev) - 1, -1, -1):
                s += prev[i].val

                if s == 0:
                    
                    if i - 1 < 0:
                        head = curr.next
                    else:
                        prev[i - 1].next = curr.next
                    
                    prev = prev[:i]
                    break
            
            curr = curr.next
        
        return head





