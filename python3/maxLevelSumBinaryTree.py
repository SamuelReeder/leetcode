# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:

        q = deque()
        curr = 0
        q.append(root)
        max_val = root.val
        max_lvl = 1
        
        while q:
            curr += 1
            val = 0

            for _ in range(len(q)):
                temp = q.popleft()

                val += temp.val

                if temp.left:
                    q.append(temp.left)

                if temp.right:
                    q.append(temp.right) 

            if val > max_val:
                max_val = val
                max_lvl = curr

        return max_lvl

            


        

        
