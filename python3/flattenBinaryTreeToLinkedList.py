# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def dfs(node):
            if node is None:
                return
            l = dfs(node.left)
            r = dfs(node.right)
            if not l:
                node.right = r
            else:
                node.right = l
                curr = node.left
                while curr.right:
                    curr = curr.right
                curr.right = r
                node.left = None
            return node

        return dfs(root)
        
        
