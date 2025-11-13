# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        
        def helper(root, parent, gp):
            if not root:
                return 0

            even = 0
            if gp is not None and gp.val % 2 == 0:
                even = root.val

            return helper(root.left, root, parent) + helper(root.right, root, parent) + even
        
        return helper(root, None, None)


