# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        # not a BST lol
        # if p.val <= root.val <= q.val or q.val <= root.val <= p.val:
        #     return root

        def helper(node):
            if not node:
                return None

            l = helper(node.left)
            r = helper(node.right)

            found = node.val == p.val or node.val == q.val
            if (r and l) or found:
                return node
            elif r:
                return r
            elif l:
                return l

        return helper(root)
                

