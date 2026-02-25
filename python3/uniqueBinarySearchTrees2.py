# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        # we loop over the root and generate each

        seen = dict()
        def helper(start, end):
            if (start, end) in seen:
                return seen[(start,end)]

            if start > end:
                return [None] 

            ls = []
            for i in range(start, end + 1):
                right = helper(i + 1, end)
                left = helper(start, i - 1)

                for l in left:
                    for r in right:
                        ls.append(TreeNode(i, l, r))

            seen[(start,end)] = ls
            return ls
        
        return helper(1, n)
                
