# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # we just inorder and if some previous was gt we have violation
        # for cases with two violations we keep inordering and swap the biggest diff
        l = r = prev = None

        def helper(node):
            nonlocal l, r, prev
            if not node:
                return

            helper(node.left)
            if prev and prev.val > node.val:
                # have a violation
                if not l:
                    l = prev
                r = node
            prev = node
            helper(node.right) 

        helper(root)

        l.val, r.val = r.val, l.val
        return root

        

