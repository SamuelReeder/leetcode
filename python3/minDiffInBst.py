# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        # right side of tree is higher
        # left is lower

        def minHelper(root):

            diff = 10**6
            high = root.val
            low = root.val

            if root.left is not None:
                diffl, highl, lowl = minHelper(root.left)
                diff = min(diff, diffl, root.val - highl)
                high = max(high, highl)
                low = min(low, lowl)

            if root.right is not None:
                diffr, highr, lowr = minHelper(root.right)
                diff = min(diff, diffr, lowr - root.val)
                high = max(high, highr)
                low = min(low, lowr)
            
            return diff, high, low

        # min is either the min of subtrees, or the diff between root and lowest on right or highest on left
        res, _, _ = minHelper(root)

        return res
