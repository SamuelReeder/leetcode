"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        if head is None:
            return head

        tmp = head

        # in first loop we do the following:
        # - we construct the basis of the deep copy
        # - we save the map of each old to new node
        # in second loop we then need to:
        # - grab the node from the hashmap
        d = dict()
        new_head = Node(head.val)
        tmp_new = new_head
        while tmp is not None:
            if tmp is not head:
                tmp_new.next = Node(tmp.val)
                tmp_new = tmp_new.next
                
            d[tmp] = tmp_new
            tmp = tmp.next
        
        tmp_new = new_head
        tmp = head
        while tmp is not None:
            if tmp.random is not None:
                tmp_new.random = d[tmp.random] # we get new node
            tmp, tmp_new = tmp.next, tmp_new.next

        return new_head

        

