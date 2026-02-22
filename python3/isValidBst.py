# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        # compare each against its ancestor bounds
        # O(n) time

        def helper(node, mi, ma):
            if node is None:
                return True

            if not (mi < node.val < ma):
                return False
            
            return helper(node.left, mi, node.val) and helper(node.right, node.val, ma)

        return helper(root, -math.inf, math.inf)
